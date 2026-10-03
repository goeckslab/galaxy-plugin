# Galaxy in Grok

Choose **Grok Build** for the plugin bundle, including the Galaxy Analysis skill, or **Grok.com** for a connection in the web chat. Both connect to the same hosted Galaxy MCP service. You do not need to deploy a server or have an AWS account.

## Grok Build: install the plugin

You need [Grok Build](https://docs.x.ai/build/overview), a maintained Node.js LTS release with `node` and `npx` available, and a browser on the same computer for authorization. Follow your organization's software policy.

1. In a terminal, install directly from GitHub:

   ```sh
   grok plugin install 'goeckslab/galaxy-plugin#plugins/galaxy-plugin'
   ```

   Review and accept the plugin trust prompt. This route does not require an xAI marketplace listing.
2. Check the installed components:

   ```sh
   grok plugin details galaxy-plugin
   grok inspect
   ```

   Confirm that Galaxy supplies one `galaxy-analysis` skill and one `galaxy` MCP connection. Do not add a second standalone Galaxy MCP connection. The client starts its connection adapter automatically; Galaxy analyses still run on the selected Galaxy site.
3. Start `grok`, open `/mcps`, select Galaxy, and choose the authentication action if requested. Complete [Galaxy authorization](#authorize-your-galaxy-account) in your browser, then return to Grok Build.
4. Start with the [read-only check](#check-the-connection). You can invoke `/galaxy-analysis` for analysis guidance; the skill and its supporting files are already included.

Grok Build is a terminal agent. Use text, tables and Galaxy source links there; this installation does not promise ChatGPT-style interactive cards. For updates, run `grok plugin update galaxy-plugin`, review the changes, and restart your session.

Official references: [plugin compatibility](https://docs.x.ai/build/features/skills-plugins-marketplaces), [plugin commands](https://docs.x.ai/build/cli/reference), and [MCP connections](https://docs.x.ai/build/features/mcp-servers).

## Grok.com: connect in web chat

This is a personal custom-connector setup, not a public-directory installation. It connects the Galaxy tools; it does not install the bundled Galaxy Analysis skill. On Business or Enterprise, an administrator must first make the connector available to the organization.

1. Sign in to [Grok Connectors](https://grok.com/connectors).
2. Choose **New Connector → Custom**. If the UI calls this **Add custom MCP**, use that option.
3. Enter these settings:

   - **Name:** `Galaxy`
   - **MCP server URL:** `https://mcp.galaxymcp.org/mcp`
   - **Authentication:** `OAuth`

   Use the automatic/published client identity when offered. Do not enter a Galaxy API key in these settings, and do not reuse the ChatGPT or Claude client ID. No client secret is needed for this public-client flow.
4. Follow the browser redirect to `https://auth.galaxymcp.org` and complete [Galaxy authorization](#authorize-your-galaxy-account).
5. Return to Grok and confirm Galaxy is connected. Open a new conversation, enable Galaxy if the interface asks, and send the [read-only check](#check-the-connection).

The service supports Grok's published web OAuth identity. Successful authorization and discovery must be followed by a real tool response; reaching a consent page alone is not a completed connection. Interactive card rendering in Grok has not been verified. Ask for text, tables and source links if cards are unavailable.

See [Grok's custom MCP connector guide](https://docs.x.ai/grok/connectors).

## Authorize your Galaxy account

1. Sign in to the Galaxy site you want to use. Open **User → Preferences → Manage API key** and reuse your existing key, or create one if you do not have one.
2. Check that the authorization page is on `https://auth.galaxymcp.org` before entering a key. Select your Galaxy sites and enter your own key for each selected site.
3. Review the requested access and retention terms, then approve. A key can allow access to your account's data and analysis operations; keep normal tool confirmations enabled. Do not use clinical or identifiable patient data in this preview.

Never put keys, OAuth tokens or passwords in chat, an MCP URL, a repository, screenshots or a public issue. Each site requires its own key; connecting several sites does not transfer data between them. Selected data and report content can be returned to Grok. Read the [service privacy notice](https://mcp.galaxymcp.org/privacy).

## Check the connection

```text
List my connected Galaxy sites and show my five most recent histories on
usegalaxy.org. Do not create histories, upload data, or run an analysis.
```

Use a site you actually authorized. Check the real tool response, not just an assistant's claim of success. In Grok Build, also confirm the installed skill with `grok plugin details galaxy-plugin`.

For an existing report, ask:

```text
Read the existing report in this history. Summarize the measured results
in a compact table and link the original report. Do not run a new analysis.
```

## Troubleshooting and disconnecting

- **Build cannot start Galaxy:** check that `node` and `npx` are available, then run `grok mcp doctor galaxy`. Restart the client after installing Node.
- **Authorization fails:** close duplicate pending Galaxy login tabs and retry one flow. Do not paste a key into chat or disable authentication.
- **No skill in Grok.com:** the custom connection supplies tools only; it is not the Build plugin bundle.
- **No cards:** use text, tables and original Galaxy links. Client UI support is separate from tool connectivity.
- **Remove access:** ask your connected assistant to manage or disconnect your Galaxy connections. Galaxy provides a private five-minute management link. To disable a key immediately, revoke it on that Galaxy site; removing a connector or plugin alone may not revoke authorization.

For installation problems, open a [GitHub issue](https://github.com/goeckslab/galaxy-plugin/issues) with the client/version, steps and a redacted error. Do not include credentials or private data. For account or privacy concerns, use the [private support contact](https://mcp.galaxymcp.org/support#private-contact).
