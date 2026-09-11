---
name: nextstep
description: Install or upgrade the NextStep conversation protocol (会话推进协议) into a repo or user-level AGENTS.md. Use ONLY for install / setup / upgrade / re-configure requests about the NextStep protocol or its capability menu. Not for daily protocol use — after install, say 菜单 or reply a number via AGENTS.md, not this skill; not for bug fixes, code writing, or unrelated tasks. 协议安装器：仅在安装/升级/配置 NextStep 协议时使用；装完即休眠，日常「菜单」与回数字走 AGENTS.md。
license: MIT
---

# NextStep

NextStep is a resident AGENTS.md protocol, not a runtime skill: at every wrap-up the assistant appends a one-line status bar and numbered next steps; capabilities are registered in a menu table and invoked by number; anti-noise and persistence rules keep it working all session under 40 lines.

This skill is the one-shot setup helper and ships both installable templates in `assets/`. After install it goes dormant by design — daily protocol use runs via AGENTS.md, not here.

## Install steps

1. Ask the user: repo-level or global?
2. Repo-level: copy the template next to this file to the project root as `AGENTS.md` — `assets/AGENTS.md` for Chinese sessions, `assets/AGENTS.en.md` for English sessions.
   Global: same content into the user-level instructions file — `~/.zcode/AGENTS.md` (ZCode) or `~/.claude/CLAUDE.md` (Claude Code).
3. If the target file already exists, merge the "Turn discipline", "Capability menu" and "Hard rules" sections into it; never overwrite the whole file. The template header states its protocol version — use it to tell upgrades from fresh installs.
4. Verify: tell the user to start a NEW session and say "menu" (or 菜单). The capability table coming back means the install worked.
5. Offer to register their first real capability in the menu table — one row: number, trigger phrase, what it does, pointer to details.

## Upgrade steps

1. Read the protocol-version line in the installed template's header; compare it with the version in `assets/`.
2. Overwrite the installed template's "Turn discipline" section and "Hard rules" section with the latest `assets/` versions — never touch the user's registered capability rows in the menu table.
3. Update the version line, then ask the user to re-verify in a NEW session with "menu" (or 菜单).

Full spec: `会话推进协议.md` at the root of the NextStep repository (not bundled in the installed skill — see the project README for the link).
