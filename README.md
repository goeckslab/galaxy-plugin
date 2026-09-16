# Galaxy

The easiest way to install is to give this prompt to your agent (replace the target app):

```text
Install Galaxy from https://github.com/goeckslab/galaxy-plugin in <target app,
such as ChatGPT Web (personal account), Claude Code, or Codex>. Follow the
repository's complete-plugin setup instructions. Install both the Galaxy tools
and the bundled galaxy-analysis skill with all its supporting files, confirm it is available,
and verify the connection with a read-only request. If my client cannot install
the complete plugin, explain the limitation; do not silently substitute tools-only access.
If you run into any problems, submit a GitHub issue at
https://github.com/goeckslab/galaxy-plugin/issues with the app/version, steps
tried, and error. Never include API keys, OAuth tokens, passwords, private
data, or chat content in the issue.
```

Work with your Galaxy data from an AI assistant. Browse analysis histories, read reports, find workflows, run bioinformatics tools and check their results. Analyses run on the Galaxy site you choose; the assistant helps you prepare them and interpret the outputs.

Choose the instructions for the app you use below; you only need one installation route. The complete plugin includes the Galaxy tools and the `galaxy-analysis` skill: instructions that help the assistant select tools, check results and record how an analysis was performed. The hosted service connects your assistant to your Galaxy account using MCP (Model Context Protocol). Connecting that service is one part of installation, not a substitute for installing the skill.

## What you need

- Your own Galaxy account and API key on one or more supported sites. An API key grants access to your Galaxy account; treat it like a password and use non-sensitive example data for your first test.
- **ChatGPT:** an account with Developer mode and access to ChatGPT Work or Codex for the Plugin Creator step. The personal local-plugin installation below uses the ChatGPT desktop app; enabling Developer mode on the web alone does not complete it. Availability depends on your account and workspace policy.
- **Claude Code or Codex:** permission to install plugins, a maintained Node.js LTS release with `node` and `npx` available to the client, and a browser on the same computer for authorization.

All routes need internet access. The Galaxy MCP service is hosted on AWS; analyses run on your chosen Galaxy site. You do not need to deploy a server, install Galaxy, run containers or have an AWS account.

## Install

### ChatGPT — complete personal plugin

Galaxy has been submitted to OpenAI and is currently under review. It is not yet listed in the public ChatGPT Plugins Directory. You can install and test a complete personal plugin before public approval by connecting the service, then packaging its skills with that connection. Follow both parts below. See [OpenAI's complete-plugin setup](https://developers.openai.com/plugins/build/plugins#create-and-test-a-plugin-locally-with-an-mcp-server).

#### 1. Connect your Galaxy account on ChatGPT Web

OpenAI documents Developer mode for personal Plus and Pro accounts; managed workspaces may restrict it. See [ChatGPT Developer mode](https://developers.openai.com/api/docs/guides/developer-mode). This step does not require Node.js or a repository download.

1. In [ChatGPT](https://chatgpt.com), open **Settings → Security and login** and enable **Developer mode**.
2. Open [Plugins](https://chatgpt.com/plugins), then select **Create app** or the **+** button to add a developer-mode app.
3. Enter these connection settings:

   - **Name:** `Galaxy`
   - **MCP server URL:** `https://mcp.galaxymcp.org/mcp`
   - **Authentication:** `OAuth`
   - **OAuth client ID:** `galaxy-chatgpt` (use the custom/static client fields if offered)
   - **OAuth client secret:** leave empty; this is a public client, not a secret to request or invent.

4. Follow [Connect your Galaxy account](#connect-your-galaxy-account) on `https://auth.galaxymcp.org`, then return to ChatGPT. Never paste a Galaxy key into a chat or the MCP URL.
5. Open the new connection's details and copy its connection ID from the browser URL for the next step. This identifies your registered connection; it is not your Galaxy API key. If you already have a working Galaxy connection, reuse it instead of creating a duplicate.

The registered ChatGPT callback is `https://chatgpt.com/connector_platform_oauth_redirect`. If ChatGPT requires a different callback or cannot use the public client settings, report the setup problem in [GitHub Issues](https://github.com/goeckslab/galaxy-plugin/issues); do not switch to unauthenticated access or reuse another client's credentials.

#### 2. Install the skill and tools as one plugin

In ChatGPT Work, give the following prompt to `@plugin-creator`, replacing `<your connection ID>`. In Codex, use `$plugin-creator` instead. The agent can download the repository for you; you do not need to edit configuration files yourself.

```text
@plugin-creator Set up the complete Galaxy personal plugin from
https://github.com/goeckslab/galaxy-plugin using my registered ChatGPT connection
<your connection ID>.
Use plugins/galaxy-plugin as the package source. Include the entire
skills/galaxy-analysis directory unchanged, including SKILL.md, agents/ and
references/. Wire this personal ChatGPT copy to my registered connection only;
do not also enable the package's separate direct MCP connection.
Add a personal local marketplace entry so I can install Galaxy in the ChatGPT
desktop app. Keep this account-specific copy local and leave the public
repository unchanged. Verify the installed skill and its supporting files,
then test the Galaxy connection with a read-only request.
```

1. Restart the ChatGPT desktop app after setup. Open **Plugins**, choose the personal local marketplace created by Plugin Creator, and install **Galaxy**.
2. Check that the installed plugin lists **Galaxy Analysis** (`galaxy-analysis`) as well as the Galaxy connection. Confirm that the skill's supporting files, including `references/runs.md` and `references/reports.md`, are present; installing only `SKILL.md` is incomplete.
3. Start a new Work conversation, select **Galaxy**, and try the [read-only example below](#try-an-existing-result-first). Keep the normal tool confirmations enabled, especially for actions that create data or start analyses.

**Using only ChatGPT Web?** Registering the connection in part 1 gives you tools, not the complete installation described here. OpenAI documents the personal local marketplace in the desktop app; do not assume a local install is also available on the web. If your web client offers a complete-plugin installation entry, verify that both the skill and connection are available there before using it. Otherwise use the desktop route above for the complete plugin; a working tools-only connection is not proof of skill installation.

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

If your workspace offers GitHub marketplace imports, ask its administrator to import this repository through **Admin → Plugins**. Packages with direct MCP configurations, including this one, are **Desktop only** in that import flow. This is separate from the personal-plugin setup above. See [ChatGPT plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Connect your Galaxy account

Find your key on the Galaxy site you want to use: sign in, then open **User → Preferences → Manage API key**. Create a key there only if you do not already have one. See [Galaxy's API key guide](https://training.galaxyproject.org/training-material/faqs/galaxy/preferences_admin_api_key.html). Keep the key out of chat, screenshots and support issues.

1. When the client starts the Galaxy connection, complete authorization in your browser. Check that the page is on `https://auth.galaxymcp.org` before entering a key.
2. Select your sites and enter **your own** Galaxy API key for each selected site. Leave unused sites empty. Do not paste keys into a chat, repository or MCP configuration.
3. Review the access and retention terms before approving. For Claude Code and Codex installations, the authorization page labels the connection **Galaxy for Claude Code**.
4. Complete the plugin-installation steps for your client, then start a new conversation and try the [read-only example](#try-an-existing-result-first). Check that `galaxy-analysis` appears in the installed plugin's skills. A working connection alone does not verify that the skill is installed. Keep the client's normal tool confirmations enabled.

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
