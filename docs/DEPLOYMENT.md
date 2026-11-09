# Publishing the static website

The \`docs/\` directory is a static HTML/CSS/JS site. It does not require VPS, a build step or paid hosting.

## GitHub Pages (after repository rename)

1. Repository **Settings → General → Repository name**: rename \`rayhan\` to \`RONICZ-GX\`.
2. **Settings → Pages → Build and deployment → Deploy from a branch**.
3. Select \`main\` and \`/docs\`, then save.
4. The expected GitHub Pages address after successful deployment is \`https://roniczai.github.io/RONICZ-GX/\`. It is **not live until GitHub confirms deployment**.

## Custom subdomain: \`gpu.ronicz.ai\`

Use your actual DNS provider (e.g., Hostinger DNS if that is managing the domain):

- Create a **CNAME** record for host \`gpu\`, pointing to \`roniczai.github.io\`.
- In GitHub Pages Settings set custom domain to \`gpu.ronicz.ai\`, then wait for DNS verification and HTTPS provisioning.
- Select **Enforce HTTPS** once available.
- GitHub may create a \`docs/CNAME\` file when the custom domain is configured. If you edit it manually, its sole content is \`gpu.ronicz.ai\`.
- Do **not** configure both conflicting A and CNAME records for \`gpu\`.

At the time of this file's creation DNS and GitHub Pages have **not** been changed. The project homepage is **not yet deployed** to the subdomain.

Alternative: deploy the contents of \`docs/\` as static files on a separate Hostinger subdomain / website. Configure DNS according to that host's actual instructions.

## Final checklist

- Replace internal GitHub links from the historical \`roniczai/rayhan\` URL with the new canonical repository URL if desired (GitHub usually redirects the old URL).
- Confirm all target labels still say research/concept.
- Verify mobile rendering, accessibility and HTTPS.
- Don't add fake product photos, sales buttons, FPS results, benchmark scores or shipping dates.

