// Captures the frames of an animated page: opens it in headless Chrome, calls renderAt(t) for every frame
// and saves each one as a PNG. Needs Node 22+ (built-in WebSocket and fetch).
// Usage: node capture.mjs <chrome> <page.html> <out-dir> <width> <height> <frames> <seconds>
import { spawn } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const [chromePath, html, outDir, W, H, N, T] = process.argv.slice(2);
const [width, height, frames, seconds] = [W, H, N, T].map(Number);
const port = 9300 + Math.floor(Math.random() * 600);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const chrome = spawn(chromePath, [
  "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
  `--remote-debugging-port=${port}`, `--window-size=${width},${height}`, `--user-data-dir=${outDir}-profile`, "about:blank",
], { stdio: "ignore" });

try {
  let wsUrl;
  for (let i = 0; i < 100 && !wsUrl; i++) {
    try {
      const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
      wsUrl = targets.find((t) => t.type === "page")?.webSocketDebuggerUrl;
    } catch {
      // Chrome is still starting
    }
    if (!wsUrl) await sleep(100);
  }
  if (!wsUrl) throw new Error("Chrome did not start");

  const ws = new WebSocket(wsUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
  let nextId = 0;
  const pending = new Map();
  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      pending.get(msg.id)(msg);
      pending.delete(msg.id);
    }
  };
  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = ++nextId;
    pending.set(id, (msg) => (msg.error ? reject(new Error(`${method}: ${msg.error.message}`)) : resolve(msg.result)));
    ws.send(JSON.stringify({ id, method, params }));
  });
  const evaluate = async (expression) =>
    (await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true })).result?.value;

  await send("Emulation.setDeviceMetricsOverride", { width, height, deviceScaleFactor: 1, mobile: false });
  await send("Page.navigate", { url: pathToFileURL(html).href });
  for (let i = 0; i < 200; i++) {
    if (await evaluate("document.readyState === 'complete' && typeof renderAt === 'function'")) break;
    await sleep(50);
  }
  await evaluate("document.fonts.ready.then(() => true)");

  rmSync(outDir, { recursive: true, force: true });
  mkdirSync(outDir, { recursive: true });
  for (let f = 0; f < frames; f++) {
    await evaluate(`renderAt(${(f / frames) * seconds})`);
    const { data } = await send("Page.captureScreenshot", { format: "png", clip: { x: 0, y: 0, width, height, scale: 1 } });
    writeFileSync(`${outDir}/frame-${String(f).padStart(4, "0")}.png`, Buffer.from(data, "base64"));
  }
  ws.close();
  console.log(`captured ${frames} frames`);
} finally {
  chrome.kill();
}
