# Galaxy

Explore your Galaxy histories, run bioinformatics analyses, check progress, and inspect results from a conversation. The bundled `galaxy-analysis` skill guides your assistant to verify live tool schemas and output evidence. The connector uses the hosted Galaxy MCP service at `https://mcp.galaxyproject.org/mcp`; analyses run on the Galaxy site you authorize, not on your computer.

Published by the Galaxy Project from Penn State University, Johns Hopkins University, Moffitt Cancer Center, and Cleveland Clinic.

## Claude chat

After installing, open the plugin's Connectors tab and connect Galaxy. On Team or Enterprise, an owner must first add the remote connector for the organization; installing the plugin alone does not add or authorize it. Sign in through the authorization page, select your Galaxy site, and supply your own Galaxy API key there. Never paste a key into chat. Start with a read-only request such as: “List my connected Galaxy sites and show my five most recent histories. Do not change anything.”

To remove a site, rotate a key or disconnect later, ask Claude in ordinary language. Galaxy will provide a private five-minute management link; no exact command or browser login cookie is required. Uninstalling the plugin alone may not revoke its existing authorization.

## Claude Code

```text
/plugin install galaxy-plugin --marketplace goeckslab/galaxy-plugin
```

Then open `/mcp` and authorize Galaxy.

## Grok Build

Install with `grok plugin install 'goeckslab/galaxy-plugin#plugins/galaxy-plugin'` and review the trust prompt. The package includes Galaxy Analysis and one Galaxy connection; do not add a duplicate MCP server. Open `/mcps` in Grok Build to authorize Galaxy, then ask for a read-only connection check. See the [Grok setup guide](https://github.com/goeckslab/galaxy-plugin/blob/main/docs/grok.md) for the full instructions and the separate Grok.com web route.

## What the plugin runs and sends

- **Claude, Codex and Grok** connect directly over HTTPS to `https://mcp.galaxyproject.org/mcp`, with authorization on the same host. They start no local program.
- **The hosted service** calls only the Galaxy sites you authorize, with your own API keys for those sites. Its tools can read your histories, datasets and reports, and can run tools and workflows within your account's permissions; keep the client's tool confirmations enabled. Galaxy data and reports you request are returned to your assistant.

Enter keys only on the authorization page, never in chat or plugin configuration. The package contains no credentials, hooks or scripts. Do not use the service for clinical or identifiable patient data. See the [privacy notice](https://mcp.galaxyproject.org/privacy), [service information](https://mcp.galaxyproject.org) and [support options](https://mcp.galaxyproject.org/support).

The plugin's text and configuration are MIT-licensed. The Galaxy logo has separate [attribution and usage conditions](assets/README.md).
