# Website deployment: RONICZ GX

The website is **source code** in \`docs/\`. The code being in a repository does not mean the page is live.

## Publish on GitHub Pages

1. Open repository [Settings → Pages](https://github.com/roniczai/Ronicz-GX/settings/pages).
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select branch **main**, folder **/docs**, and Save.
4. Wait for a successful Pages deployment in GitHub. **Only then** test the GitHub Pages URL: \`https://roniczai.github.io/Ronicz-GX/\`.

## Optional custom domain: \`gpu.ronicz.ai\`

1. Confirm which DNS provider currently manages the nameservers for \`ronicz.ai\`.
2. In GitHub Pages settings, enter the custom domain: \`gpu.ronicz.ai\`.
3. In the actual DNS provider, add a CNAME: \`gpu\` → \`roniczai.github.io\`. Avoid conflicting A/AAAA/CNAME records for the same hostname.
4. Allow DNS and GitHub domain validation to complete. Turn on **Enforce HTTPS** when available.
5. GitHub typically writes a \`docs/CNAME\` file after configuration. If necessary, its entire content is the hostname \`gpu.ronicz.ai\`.

**Neither Pages nor the custom DNS was configured by committing these files.** Live hosting must be verified separately.

## Site quality checklist

- Mobile and desktop visual inspection.
- No product ordering, fake benchmarks, fabricated hardware photos or misleading launch language.
- Verify links, favicon, page title and SEO descriptions.
- Keep research evidence and milestone status current.
- Ensure HTTPS before publicly sharing a custom domain.

