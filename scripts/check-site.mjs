// Sanity checks for the static site: every local file the page references exists,
// and the hand-written JSON (structured data, web manifest) parses.
import { readFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";

const errors = [];
const html = readFileSync("index.html", "utf8");

// 1. Local src/href references in index.html
const isLocal = (url) => !/^(https?:|mailto:|tel:|#|data:)/i.test(url);
// Resolve a URL as the browser would: "/x" from the site root, "x" relative to the referring file's folder.
const resolve = (fromDir, url) => {
  const path = url.split(/[?#]/)[0];
  return path.startsWith("/") ? `.${path}` : join(fromDir, path);
};
for (const [, url] of html.matchAll(/\b(?:src|href)="([^"]+)"/g)) {
  if (isLocal(url) && !existsSync(resolve(".", url))) {
    errors.push(`index.html references missing file: ${url}`);
  }
}

// 2. JSON-LD blocks must be valid JSON
for (const [, json] of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
  try {
    JSON.parse(json);
  } catch (e) {
    errors.push(`Invalid JSON-LD: ${e.message}`);
  }
}

// 3. Web manifest must parse and its icons must exist (paths are relative to the manifest)
const manifestPath = "assets/img/favicon/site.webmanifest";
try {
  const manifest = JSON.parse(readFileSync(manifestPath, "utf8"));
  for (const icon of manifest.icons ?? []) {
    if (!existsSync(resolve(dirname(manifestPath), icon.src))) {
      errors.push(`${manifestPath} references missing icon: ${icon.src}`);
    }
  }
} catch (e) {
  errors.push(`Invalid ${manifestPath}: ${e.message}`);
}

// 4. url(...) references in the built CSS (fonts) must exist
const cssPath = "assets/css/style.css";
const css = readFileSync(cssPath, "utf8");
for (const [, url] of css.matchAll(/url\(["']?([^"')]+)["']?\)/g)) {
  if (isLocal(url) && !existsSync(resolve(dirname(cssPath), url))) {
    errors.push(`${cssPath} references missing file: ${url}`);
  }
}

if (errors.length) {
  console.error(errors.map((e) => `✖ ${e}`).join("\n"));
  process.exit(1);
}
console.log("✔ Site checks passed");
