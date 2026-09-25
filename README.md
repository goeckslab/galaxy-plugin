# Galaxy

**Turn your ChatGPT chat into a Galaxy agent.**

The easiest way to install is to give this prompt to your agent (replace the target app):

```text
Install Galaxy from https://github.com/goeckslab/galaxy-plugin in <target app,
such as ChatGPT Web (Chat or Work), Claude Code, or Codex>. Follow the
repository's setup instructions for that app. Install both the Galaxy tools
and the bundled galaxy-analysis skill with all its supporting files, confirm it is available,
and verify the connection with a read-only request. If my client cannot make
both available, explain the limitation; do not silently substitute tools-only access.
If you run into any problems, submit a GitHub issue at
https://github.com/goeckslab/galaxy-plugin/issues with the app/version, steps
tried, and error. Never include API keys, OAuth tokens, passwords, private
data, or chat content in the issue.
```

Work with your Galaxy data from an AI assistant. Browse analysis histories, read reports, find workflows, run bioinformatics tools and check their results. Analyses run on the Galaxy site you choose; the assistant helps you prepare them and interpret the outputs.

Choose the instructions for the app you use below; you only need one installation route. The setup has two parts: the Galaxy connection supplies tools, and the `galaxy-analysis` skill provides guidance for using them and checking results. In ChatGPT Web, whether you use Chat or Work, connect the service and upload the skill separately. Claude Code and Codex install both through their plugin package. The hosted service connects your assistant to your Galaxy account using MCP (Model Context Protocol).

<a id="watch-the-chatgpt-web-walkthroughs"></a>

## Watch the walkthroughs

Play the videos directly below. All three include English narration and captions.

### Set up Galaxy in ChatGPT Web · 5:00

Add Galaxy with its logo, authorize your Galaxy account, upload the Galaxy Analysis skill and check the connection in a new Chat.

https://github.com/user-attachments/assets/b7f7f3ee-514e-4415-b20d-f9abdeff5d62

The installation video shows the current personal Web setup while the plugin awaits OpenAI review. It requires Developer mode and skill uploads on your account; it is not a public-directory installation.

### Run an analysis in ChatGPT · 2:41

Start a real paired-end read analysis, browse its history cards, inspect an HTML report preview and open the original interactive report in Galaxy.

https://github.com/user-attachments/assets/bac7c2f2-6f52-4858-9783-f094a3f3be64

### Run an analysis in Claude Desktop · 3:14

With Galaxy already connected, analyze public yeast count data, check run status, browse files, preview a results table and open the original PDF report in Galaxy.

https://github.com/user-attachments/assets/d1926a8e-af6b-4105-b804-54470619ff87

The two demos focus on using the product and inspecting its outputs, not interpreting the scientific results.

## What you need

- Your own Galaxy account and API key on one or more supported sites. An API key grants access to your Galaxy account; treat it like a password and use non-sensitive example data for your first test.
- **ChatGPT Web (Chat or Work):** sign in to an account with **Developer mode** and **Skills → Upload from your computer** available. Both are needed for the browser setup with tools and the skill shown in the video. Availability depends on your account and workspace policy; this route does not require the desktop app, Plugin Creator or Codex.
- **Claude Code or Codex:** permission to install plugins, a maintained Node.js LTS release with `node` and `npx` available to the client, and a browser on the same computer for authorization.

All routes need internet access. The Galaxy MCP service is hosted on AWS; analyses run on your chosen Galaxy site. You do not need to deploy a server, install Galaxy, run containers or have an AWS account.

## Install

### ChatGPT Web — Chat or Work

Galaxy has been submitted to OpenAI and is currently under review. It is not yet listed in the public ChatGPT Plugins Directory. The browser setup below matches the installation video: add the Galaxy connection, upload Galaxy Analysis, then use both in a new **Chat or Work** conversation. These are two separate installations, not a single uploaded plugin package. The video uses Chat, but [OpenAI also documents using a personal MCP connection in Work on the web](https://developers.openai.com/plugins/quickstart); Plugin Creator and a desktop plugin are not prerequisites for this browser route.

Before starting, sign in to ChatGPT and check that your account offers both Developer mode and a skill-upload control under **Plugins → Skills**. The upload route was verified on the account used for the walkthrough; it is not a guarantee of availability on every account. If skill upload is missing, consider the optional desktop setup below. If Developer mode is unavailable, check with your workspace administrator or use Claude Code or Codex. Attaching the ZIP to an ordinary chat does not install the skill.

#### 1. Prepare the Galaxy Analysis skill

1. At the top of [this repository](https://github.com/goeckslab/galaxy-plugin), choose **Code → Download ZIP**, then extract the download.
2. Open `plugins/galaxy-plugin/skills/` and locate the `galaxy-analysis` folder.
3. Compress the **whole `galaxy-analysis` folder** into `galaxy-analysis.zip`. Keep its contents unchanged: `SKILL.md`, `agents/openai.yaml`, `references/runs.md` and `references/reports.md`.

Upload this skill ZIP in step 3, not the whole repository archive or just `SKILL.md`.

#### 2. Connect your Galaxy account

If Galaxy is already connected on this account, reuse it instead of creating a duplicate. OpenAI documents Developer mode for personal Plus and Pro accounts; managed workspaces may restrict it. See [ChatGPT Developer mode](https://developers.openai.com/api/docs/guides/developer-mode).

1. In [ChatGPT](https://chatgpt.com), open **Settings → Security and login** and enable **Developer mode**.
2. Open [Plugins](https://chatgpt.com/plugins), then select **Create app** or the **+** button to add a developer-mode app.
3. Enter these connection settings:

   - **Name:** `Galaxy`
   - **Icon:** upload [`galaxy-logo.png`](plugins/galaxy-plugin/assets/galaxy-logo.png) from `plugins/galaxy-plugin/assets/` in the extracted download. This is the Galaxy logo used for the submitted plugin and fits the form's 10 KB PNG limit.
   - **MCP server URL:** `https://mcp.galaxymcp.org/mcp`
   - **Authentication:** `OAuth`
   - **OAuth client ID:** `galaxy-chatgpt` (use the custom/static client fields if offered)
   - **OAuth client secret:** leave empty; this is a public client, not a secret to request or invent.

4. Follow [Connect your Galaxy account](#connect-your-galaxy-account) on `https://auth.galaxymcp.org`, then return to ChatGPT. Never paste a Galaxy key into a chat or the MCP URL.
5. Confirm that the Galaxy connection is installed and connected. If its details offer **Connect** or **Sign in with Galaxy**, finish that authorization before continuing.

The registered ChatGPT callback is `https://chatgpt.com/connector_platform_oauth_redirect`. If ChatGPT requires a different callback or cannot use the public client settings, report the setup problem in [GitHub Issues](https://github.com/goeckslab/galaxy-plugin/issues); do not switch to unauthenticated access or reuse another client's credentials.

#### 3. Upload Galaxy Analysis

1. Return to **Plugins → Skills** in ChatGPT Web.
2. Choose **Create** or the **+** button, then **Upload from your computer**.
3. Select `galaxy-analysis.zip` and wait for **Skill uploaded**.
4. Open **Galaxy Analysis** and confirm it is installed. Its files should include `SKILL.md`, `agents/openai.yaml` and both files under `references/`.

If Galaxy Analysis is already installed, inspect and reuse it; do not delete it or upload a duplicate just to follow the video.

#### 4. Check both in a new Chat or Work conversation

1. Start a new **Chat** or **Work** conversation on ChatGPT Web. Use Chat for the walkthrough as recorded; Work is also a browser option if it is available on your account.
2. Select both **Galaxy** and **Galaxy Analysis** using the available plugin/skill controls (in Work, you can use `@` to select the Galaxy connection). Keep the normal tool confirmations enabled. If either component is unavailable in your chosen mode, do not treat the complete setup as verified.
3. Ask for a read-only connection check:

   ```text
   Check my Galaxy connection and tell me which sites are connected.
   Do not create histories, upload data or run an analysis.
   ```

Check the real tool response and site names. A successful connection check does not by itself prove that the skill is installed; verify the installed skill and its supporting files in step 3. You can then [browse an existing result](#try-an-existing-result-first) or follow the analysis demo above.

<details>
<summary>Optional: install a combined personal plugin in ChatGPT Desktop</summary>

This is a separate installation route, not an extra step for ChatGPT Web in either Chat or Work. It requires the ChatGPT desktop app and access to ChatGPT Work or Codex for Plugin Creator. See [OpenAI's local-plugin setup](https://developers.openai.com/plugins/build/plugins#create-and-test-a-plugin-locally-with-an-mcp-server).

First register or reuse the Galaxy connection using step 2 above. Open its details and copy its connection ID from the browser URL. This identifies the registered connection; it is not your Galaxy API key.

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

Installing this local desktop package does not by itself verify that the complete plugin is available on the web. If the registered Galaxy connection appears in the same signed-in ChatGPT account on the web, reuse it; follow the Web steps above to check that Galaxy Analysis is available there too.

</details>

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
4. Return to the setup steps for your client and finish installing Galaxy Analysis. Check that both the Galaxy connection and the skill are available in a new conversation, then try the [read-only example](#try-an-existing-result-first). A working connection alone does not verify that the skill is installed. Keep the client's normal tool confirmations enabled.

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

- **No Plugin Creator in ChatGPT Web:** follow the ChatGPT Web steps above; Plugin Creator is only part of the optional combined desktop-plugin route. Sign in first, then check whether your account exposes Developer mode and skill upload.
- **Command not found (desktop):** ensure the desktop app can find `node` and `npx`; restart it after installing Node. Follow your organization's software policy. These commands are not needed for ChatGPT Web.
- **Authorization fails:** use the settings for your target client. ChatGPT Web uses `galaxy-chatgpt` and its HTTPS callback above; the Claude Code and Codex packages use port **3118** and `/callback`. Do not interchange them. Complete one login at a time and close another pending Galaxy authorization before retrying.
- **Duplicate tools:** keep only the intended Galaxy connection enabled in the client. Do not overwrite unrelated MCP settings.
- **Missing cards:** ask for a text summary and source links; card support varies by client.
- **Analysis still running:** ask for the status of the existing run. An accepted submission is not a completed analysis; do not submit it again just because results are not ready.
- **Unsupported action:** the service exposes selected Galaxy operations, not arbitrary scripts or the entire Galaxy API. Ask for an explanation of the available alternatives.

## Support and credits

For bugs, installation help or site requests, open a [GitHub issue](https://github.com/goeckslab/galaxy-plugin/issues) with your app/version, reproduction steps and a redacted error, or the public site details. Issues are public; do not include credentials, private datasets or chat content. For privacy, deletion or account concerns, use the [private contact form](https://mcp.galaxymcp.org/support#private-contact). It is hosted by Google Forms; responses are not published. Service information: [Galaxy MCP](https://mcp.galaxymcp.org).

Maintained by JUNHAO QIU. See the Galaxy logo's [attribution and usage conditions](plugins/galaxy-plugin/assets/README.md).
