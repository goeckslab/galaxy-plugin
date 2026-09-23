#!/usr/bin/env python3
"""Validate Galaxy plugin catalogs, connection settings and the public file inventory."""

import argparse
import json
import re
from pathlib import Path

NAME = "galaxy-plugin"
PLUGIN = f"plugins/{NAME}"
FILES = {
    "README.md", ".gitignore", ".github/workflows/check.yml",
    ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
    "scripts/check_package.py",
    f"{PLUGIN}/.codex-plugin/plugin.json", f"{PLUGIN}/.claude-plugin/plugin.json",
    f"{PLUGIN}/.mcp.json", f"{PLUGIN}/skills/galaxy-analysis/SKILL.md",
    f"{PLUGIN}/skills/galaxy-analysis/agents/openai.yaml",
    f"{PLUGIN}/skills/galaxy-analysis/references/runs.md",
    f"{PLUGIN}/skills/galaxy-analysis/references/reports.md",
    f"{PLUGIN}/assets/README.md", f"{PLUGIN}/assets/galaxy-directory.png",
    f"{PLUGIN}/assets/galaxy-logo.png",
}
MCP = {"mcpServers": {"galaxy": {
    "command": "npx",
    "args": ["--yes", "mcp-remote@0.8.3", "https://mcp.galaxymcp.org/mcp", "3118",
             "--resource", "https://mcp.galaxymcp.org/mcp",
             "--callback-path", "/callback", "--transport", "http-only",
             "--static-oauth-client-info",
             '{"client_id":"galaxy-claude-code","token_endpoint_auth_method":"none"}',
             "--auth-timeout", "300", "--silent"],
}}}
PRIVATE = re.compile(
    r"/(?:Users|home|private)/|[A-Za-z]:\\(?:Users|Documents)\\|"
    r"https://(?:chatgpt\.com/c/|claude\.ai/chat/)|asdk_app_[A-Za-z0-9_]+|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[A-Z0-9]{16}|"
    r"(?:gh[pousr]_|sk-)[A-Za-z0-9_-]{20,}|"
    r'"(?:api_key|access_token|refresh_token|client_secret|password)"\s*:\s*"[^"\s]+"'
)


def validate(files):
    assert set(files) == FILES, "Public file inventory changed; review the allowlist"
    for name, data in files.items():
        if name.endswith(".png"):
            assert data.startswith(b"\x89PNG\r\n\x1a\n"), "Invalid logo"
        else:
            assert not PRIVATE.search(data.decode()), f"Potential private content in {name}"
    read = lambda name: json.loads(files[name])
    assert len(files[f"{PLUGIN}/assets/galaxy-logo.png"]) <= 10000, "Personal connection icon exceeds 10 KB"
    codex = read(f"{PLUGIN}/.codex-plugin/plugin.json")
    claude = read(f"{PLUGIN}/.claude-plugin/plugin.json")
    assert codex["name"] == claude["name"] == NAME
    assert codex["version"] == claude["version"]
    assert "apps" not in codex and "apps" not in claude, "No private app mapping"
    assert codex["skills"] == "./skills/"
    assert codex["mcpServers"] == claude["mcpServers"] == "./.mcp.json"
    for icon in ("logo", "composerIcon"):
        assert codex["interface"][icon] == "./assets/galaxy-directory.png"
    assert read(f"{PLUGIN}/.mcp.json") == MCP, "OAuth/endpoint/dependency contract changed"
    for path, source in (
        (".agents/plugins/marketplace.json", {"source": "local", "path": f"./{PLUGIN}"}),
        (".claude-plugin/marketplace.json", f"./{PLUGIN}"),
    ):
        catalog = read(path)
        assert catalog["name"] == "galaxy-plugins"
        assert len(catalog["plugins"]) == 1
        entry = catalog["plugins"][0]
        assert entry["name"] == NAME and entry["source"] == source
        if path.startswith(".agents/"):
            assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    skill = files[f"{PLUGIN}/skills/galaxy-analysis/SKILL.md"].decode()
    assert skill.startswith("---\nname: galaxy-analysis\ndescription:")
    assert "get_galaxy_connections" in skill and "read_dataset_report" in skill
    reference_root = f"{PLUGIN}/skills/galaxy-analysis/"
    targets = {reference_root + target for target in re.findall(r"\]\((references/[^)#\s]+)\)", skill)}
    references = {name for name in files if name.startswith(reference_root + "references/")}
    assert targets == references, "Skill references must be bundled and reachable from SKILL.md"
    for name in references:
        assert files[name].strip(), f"Empty skill reference: {name}"
        for target in re.findall(r"\]\(([^)\s]+\.md)\)", files[name].decode()):
            if "://" not in target:
                assert (Path(name).parent / target).as_posix() in files, f"Broken skill reference: {name} -> {target}"


def check(root):
    files = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts[0] == ".git":
            continue
        assert not path.is_symlink(), f"Symlink is not distributable: {relative}"
        if path.is_file():
            files[relative.as_posix()] = path.read_bytes()
    validate(files)
    print(f"Public package checks passed ({len(files)} files).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    check(parser.parse_args().root)
