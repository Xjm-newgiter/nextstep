---
name: nextstep
description: Install or upgrade the NextStep conversation protocol (会话推进协议) into a repo or user-level AGENTS.md. Use ONLY for install, setup, upgrade or re-configure requests about the NextStep protocol or its capability menu. Not for daily protocol use, and once installed, say 菜单 or reply with a number through AGENTS.md rather than through this skill. Not for bug fixes, code writing, or unrelated tasks. 协议安装器：仅在安装、升级、配置 NextStep 协议时使用；装完即休眠，日常「菜单」与回数字走 AGENTS.md。
license: MIT
---

# NextStep

NextStep is a resident `AGENTS.md` protocol rather than a runtime skill. At the end of each work round the assistant adds a status line and numbered next steps. Capabilities live in a table and get invoked by number. Anti-noise and persistence rules keep the whole thing under 40 lines.

This skill is the one-shot setup helper. It ships both installable templates in `templates/` and goes dormant after install, by design. Day to day use runs through `AGENTS.md`.

## Install steps

1. Ask the user whether this is for one repository or for their whole machine.
2. Copy the template that sits in `templates/` next to this file to the project root as `AGENTS.md`. Use `templates/AGENTS.md` for Chinese sessions and `templates/AGENTS.en.md` for English ones.
   For the whole machine, put the same content in the user-level instructions file: `~/.zcode/AGENTS.md` for ZCode, or `~/.claude/CLAUDE.md` for Claude Code.
3. If the target file already exists, merge the turn discipline, capability menu and hard rules sections into it. Never replace the whole file. The template header carries its protocol version, which tells upgrades apart from fresh installs.
4. Verify by asking the user to start a new session and say "menu" (or 菜单). The capability table coming back means the install worked.
5. Offer to register their first real capability: one row with a number, a trigger phrase, what it does, and where the detail lives.

## Upgrade steps

1. Read the protocol version in the installed template's header and compare it with the one in `templates/`.
2. Overwrite the installed template's turn discipline and hard rules sections with the latest copies from `templates/`. Leave the user's registered capability rows alone.
3. Update the version line, then ask the user to re-verify in a new session with "menu" (or 菜单).

The full spec is `会话推进协议.md` at the root of the NextStep repository. It is not bundled with the skill, so point the user at the project README for the link.
