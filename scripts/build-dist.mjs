// Copies only the files that belong on the web server into dist/.
// Anything not listed here (node_modules, sources, configs, README...) is never uploaded.
import { cpSync, rmSync, mkdirSync } from "node:fs";

const files = [
  "index.html",
  ".htaccess",
  "favicon.ico",
  "robots.txt",
  "sitemap.xml",
  "assets/css/style.css",
  "assets/fonts",
  "assets/img",
];

rmSync("dist", { recursive: true, force: true });
mkdirSync("dist");
for (const path of files) {
  cpSync(path, `dist/${path}`, { recursive: true });
}
console.log(`✔ dist/ ready (${files.length} entries)`);
