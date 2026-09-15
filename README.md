# Galaxy

The easiest way to install is to give this prompt to your agent (replace the target app):

```text
Install Galaxy from https://github.com/goeckslab/galaxy-plugin in <target app,
such as ChatGPT Web (personal account), Claude Code, or Codex>. Follow the
repository's setup instructions. Install the bundled galaxy-analysis skill where
supported, confirm it is available, and verify the connection with a read-only
request. If the route connects tools without installing the skill, tell me clearly.
If you run into any problems, submit a GitHub issue at
https://github.com/goeckslab/galaxy-plugin/issues with the app/version, steps
tried, and error. Never include API keys, OAuth tokens, passwords, private
data, or chat content in the issue.
```

Work with your Galaxy data from an AI assistant. Browse analysis histories, read reports, find workflows, run bioinformatics tools and check their results. Analyses run on the Galaxy site you choose; the assistant helps you prepare them and interpret the outputs.

Choose the instructions for the app you use below; you only need one installation route. The hosted service connects that app to your Galaxy account using MCP (Model Context Protocol). Claude Code and Codex package installs also include the `galaxy-analysis` skill: instructions that help the assistant select tools, check results and record how an analysis was performed. The ChatGPT Web connection supplies tools and compatible cards, but does not automatically install that skill.

## What you need

- Your own Galaxy account and API key on one or more supported sites. An API key grants access to your Galaxy account; treat it like a password and use non-sensitive example data for your first test.
- **ChatGPT Web:** a personal Plus or Pro account with Developer mode available. No repository download or Node.js installation is needed.
- **Claude Code or Codex:** permission to install plugins, a maintained Node.js LTS release with `node` and `npx` available to the client, and a browser on the same computer for authorization.

All routes need internet access. The Galaxy MCP service is hosted on AWS; analyses run on your chosen Galaxy site. You do not need to deploy a server, install Galaxy, run containers or have an AWS account.

## Install

### ChatGPT Web — personal account

Galaxy has been submitted to OpenAI and is currently under review. It is not yet listed in the public ChatGPT Plugins Directory. In the meantime, eligible personal accounts can use the instructions below to connect directly through Developer mode.

This route does not require an organization administrator or a GitHub marketplace import. OpenAI documents Developer mode for personal Plus and Pro accounts on the web; if the option is unavailable, check your account's eligibility. See [ChatGPT Developer mode](https://developers.openai.com/api/docs/guides/developer-mode).

1. In [ChatGPT](https://chatgpt.com), open **Settings → Security and login** and enable **Developer mode**.
2. Open [Plugins](https://chatgpt.com/plugins), then select **Create app** or the **+** button to add a developer-mode app.
3. Enter these connection settings:

   - **Name:** `Galaxy`
   - **MCP server URL:** `https://mcp.galaxymcp.org/mcp`
   - **Authentication:** `OAuth`
   - **OAuth client ID:** `galaxy-chatgpt` (use the custom/static client fields if offered)
   - **OAuth client secret:** leave empty; this is a public client, not a secret to request or invent.

4. Follow [Connect your Galaxy account](#connect-your-galaxy-account) on `https://auth.galaxymcp.org`, then return to ChatGPT. Never paste a Galaxy key into a chat or the MCP URL.
5. Start a conversation, choose **Developer mode** from the **+** menu, select **Galaxy**, and try the [read-only example below](#try-an-existing-result-first).

The registered ChatGPT callback is `https://chatgpt.com/connector_platform_oauth_redirect`. If ChatGPT requires a different callback or cannot use the public client settings, report the setup problem in [GitHub Issues](https://github.com/goeckslab/galaxy-plugin/issues); do not switch to unauthenticated access or reuse another client's credentials.

This connects the hosted tools, their usage guidance and compatible cards to your own account; it does not import the repository's full `galaxy-analysis` skill. Keep the normal tool confirmations enabled, especially for actions that create data or start analyses.

### Claude Code

In Claude Code, run these two commands. The client downloads the package from GitHub; no manual repository download is needed.

```text
/plugin marketplace add goeckslab/galaxy-plugin
/plugin install galaxy-plugin@galaxy-plugins
```

Follow the activation prompt, then use `/mcp` to complete [Galaxy authorization](#connect-your-galaxy-account). The default installation is for your own user account. This installs both the connection and the skill; you do not need to import the skill separately. See [Claude plugin installation](https://code.claude.com/docs/en/discover-plugins).

### Codex

In a terminal, run these two commands. Codex downloads the package from GitHub; no manual repository download is needed.

```sh
codex plugin marketplace add goeckslab/galaxy-plugin
codex plugin add galaxy-plugin@galaxy-plugins
```

Complete the setup prompts. This installs both the connection and the skill. If your version does not recognize `codex plugin add`, open the plugin browser in Codex (or `/plugins` in its CLI), select **Galaxy** from **galaxy-plugins**, and install. Adding the catalog alone does not install the plugin. See [OpenAI plugin installation and distribution](https://developers.openai.com/plugins/build/plugins).

### ChatGPT workspace marketplace import

If your workspace offers GitHub marketplace imports, ask its administrator to import this repository through **Admin → Plugins**. Packages with direct MCP configurations, including this one, are **Desktop only** in that import flow. This restriction does not prevent the separate personal ChatGPT Web connection above. See [ChatGPT plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Connect your Galaxy account

Find your key on the Galaxy site you want to use: sign in, then open **User → Preferences → Manage API key**. Create a key there only if you do not already have one. See [Galaxy's API key guide](https://training.galaxyproject.org/training-material/faqs/galaxy/preferences_admin_api_key.html). Keep the key out of chat, screenshots and support issues.

1. When the client starts the Galaxy connection, complete authorization in your browser. Check that the page is on `https://auth.galaxymcp.org` before entering a key.
2. Select your sites and enter **your own** Galaxy API key for each selected site. Leave unused sites empty. Do not paste keys into a chat, repository or MCP configuration.
3. Review the access and retention terms before approving. For Claude Code and Codex installations, the authorization page labels the connection **Galaxy for Claude Code**.
4. Start a new conversation and try the [read-only example](#try-an-existing-result-first). For Claude Code and Codex package installs, also check that `galaxy-analysis` appears in the installed plugin's skills. A working connection alone does not verify that the skill is installed. Keep the client's normal tool confirmations enabled.

You can connect accounts on the US (`usegalaxy.org`), Europe (`usegalaxy.eu`), Australia (`usegalaxy.org.au`), France (`usegalaxy.fr`) and Canada (`usegalaxy.ca`) sites. Need another site? [Request its addition](https://mcp.galaxymcp.org/support#request-site) through GitHub Issues. Include only public site information, never credentials or private data.

Each selected site needs its own account key, even when you connect several sites in one authorization. Data is not automatically copied between sites. Selected data and report content are returned to your assistant; read the [service privacy notice](https://mcp.galaxymcp.org/privacy). This preview is not intended for clinical, identifiable patient or other regulated data.

The authorization service retains Galaxy keys under the consent terms; Claude Code and Codex installations also cache OAuth credentials locally. Uninstalling the plugin does not necessarily revoke authorization. To withdraw access, use the available revocation controls or rotate your Galaxy key.

## Try an existing result first

```text
List my connected Galaxy sites and ask me which one to use. Then show my five
most recent histories there, without creating or changing anything.
```

Choose a history to inspect. If it contains a FastQC report, try:

```text
Read the existing FastQC report in this history. Summarize its measured QC
metrics and warnings in a compact table, show relevant figures if this client
supports them, and link the source report. Do not run a new analysis.
```

Interactive history, report and status cards require compatible MCP UI support in your client. HTML reports appear as static previews; use the source links to open the originals in Galaxy. Clients without card support can use report text, tables and links. Check the source evidence when interpreting results: an assistant's summary is not a substitute for scientific validation.

## Troubleshooting and limits

- **Command not found (desktop):** ensure the desktop app can find `node` and `npx`; restart it after installing Node. Follow your organization's software policy. These commands are not needed for ChatGPT Web.
- **Authorization fails:** use the settings for your target client. ChatGPT Web uses `galaxy-chatgpt` and its HTTPS callback above; the Claude Code and Codex packages use port **3118** and `/callback`. Do not interchange them. Complete one login at a time and close another pending Galaxy authorization before retrying.
- **Duplicate tools:** keep only the intended Galaxy connection enabled in the client. Do not overwrite unrelated MCP settings.
- **Missing cards:** ask for a text summary and source links; card support varies by client.
- **Analysis still running:** ask for the status of the existing run. An accepted submission is not a completed analysis; do not submit it again just because results are not ready.
- **Unsupported action:** the service exposes selected Galaxy operations, not arbitrary scripts or the entire Galaxy API. Ask for an explanation of the available alternatives.

## Support and credits

For bugs, installation help or site requests, open a [GitHub issue](https://github.com/goeckslab/galaxy-plugin/issues) with your app/version, reproduction steps and a redacted error, or the public site details. Issues are public; do not include credentials, private datasets or chat content. For privacy, deletion or account concerns, use the [private contact form](https://mcp.galaxymcp.org/support#private-contact). It is hosted by Google Forms; responses are not published. Service information: [Galaxy MCP](https://mcp.galaxymcp.org).

Maintained by JUNHAO QIU. See the Galaxy logo's [attribution and usage conditions](plugins/galaxy-plugin/assets/README.md).
