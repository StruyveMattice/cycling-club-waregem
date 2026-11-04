# Website Cycling Club Waregem

The official website of Cycling Club Waregem, a recreational cycling club in the city of Waregem, Belgium.
Live at [cyclingclubwaregem.be](https://cyclingclubwaregem.be).

This single page website is a side project built with plain HTML and [Tailwind CSS](https://tailwindcss.com).

## Development

```bash
npm install
npm run dev     # rebuilds assets/css/style.css on every change
npm run build   # minified production build
```

Open `index.html` in a browser to preview.

`assets/css/style.css` is committed, so run `npm run build` after changing classes or `input.css` and commit the result. CI fails if you forget.

```bash
npm test        # HTML validation + checks that every referenced file exists and the JSON is valid
npm run dist    # builds the CSS and copies only the public files into dist/
```

## CI and deployment

GitHub Actions does the checks and the upload, so there's no more manual FTP.

| Workflow | When | What |
|---|---|---|
| `ci.yml` | Every pull request | Checks the committed CSS is up to date, validates the HTML, checks file references, JSON-LD and the manifest |
| `deploy.yml` | Every push to `main` (or the **Run workflow** button) | Runs the same checks, then uploads `dist/` to OVH over SFTP and checks the live site responds |

Dependabot opens a pull request once a month when the actions or npm packages have updates.

### One-time setup

1. **Enable SFTP on OVH.** In the OVHcloud Control Panel go to *Web Cloud → Hosting plans → your plan → FTP-SSH*. Make sure SFTP is enabled for your FTP user. Note the server address (e.g. `ftp.cluster0XX.hosting.ovh.net`) and the login.
2. **Get the server's host key.** Run this once, so the deploy only ever talks to the real OVH server:

   ```bash
   ssh-keyscan ftp.cluster0XX.hosting.ovh.net
   ```

3. **Add repository secrets.** On GitHub go to *Settings → Secrets and variables → Actions → New repository secret*:

   | Secret | Value |
   |---|---|
   | `SFTP_HOST` | the server address from step 1 |
   | `SFTP_USERNAME` | your FTP login |
   | `SFTP_PASSWORD` | your FTP password |
   | `SFTP_KNOWN_HOSTS` | the full output of `ssh-keyscan` from step 2 |

4. **Optional.** If the site doesn't live in `www` on the server, add a repository *variable* `SFTP_REMOTE_DIR` with the right folder.

The deploy uploads and overwrites files but never deletes anything on the server. Remove old files by hand if needed.

## Structure

- `index.html`: the whole site
- `assets/css/input.css`: Tailwind source (theme colours, fonts, custom utilities)
- `assets/fonts/`: self-hosted Bebas Neue and Roboto (SIL Open Font License)
- `.htaccess`: HTTPS and non-www redirect, caching and security headers (Apache / OVH)
- `scripts/`: site checks and the `dist/` builder used by CI
- `.github/`: CI, deploy and Dependabot configuration

## Contributing

Contributions are always welcome!

## License

[MIT](https://choosealicense.com/licenses/mit/)
