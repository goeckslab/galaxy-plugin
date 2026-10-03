# Galaxy

Explore your Galaxy histories, run bioinformatics analyses, check progress, and inspect results from a conversation. The bundled `galaxy-analysis` skill guides your assistant to verify live tool schemas and output evidence. The connector uses the hosted Galaxy MCP service; analyses run on the Galaxy site you authorize, not on your computer.

## Grok Build

Install with `grok plugin install 'goeckslab/galaxy-plugin#plugins/galaxy-plugin'` and review the trust prompt. The package includes Galaxy Analysis and one Galaxy connection; do not add a duplicate MCP server. A maintained Node.js LTS release with `node` and `npx` is required for the connection adapter. Open `/mcps` in Grok Build to authorize Galaxy, then ask for a read-only connection check. Use text, tables and Galaxy links in the terminal. See the [Grok setup guide](https://github.com/goeckslab/galaxy-plugin/blob/main/docs/grok.md) for the full instructions and the separate Grok.com web route.

## Claude chat

After installing, open the plugin's Connectors tab and connect Galaxy. Sign in through the authorization page, select your Galaxy site, and supply your own Galaxy API key there. Never paste a key into chat. Start with a read-only request such as: “List my connected Galaxy sites and show my five most recent histories. Do not change anything.”

The service can access only the Galaxy sites and account permissions you authorize. It may return history contents, reports, and links to Claude; do not use it for clinical or identifiable patient data. See the [privacy notice](https://mcp.galaxymcp.org/privacy), [service information](https://mcp.galaxymcp.org), and [support options](https://mcp.galaxymcp.org/support).

The plugin's text and configuration are MIT-licensed. The Galaxy logo has separate [attribution and usage conditions](assets/README.md).
