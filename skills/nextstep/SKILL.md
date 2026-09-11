---
name: nextstep
description: Install and manage the NextStep conversation protocol (会话推进协议). Use when the user wants to install NextStep, add a "reply with a number" turn scaffold or numbered capability menu to their AI assistant, register capabilities in AGENTS.md, or asks about the NextStep protocol. 给 AI 编码助手安装"选项递到眼前、回一个数字就能推进"的会话推进协议。
license: MIT
---

# NextStep

NextStep is a resident AGENTS.md protocol, not a runtime skill: at every wrap-up the assistant appends a one-line status bar and numbered next steps; capabilities are registered in a menu table and invoked by number; anti-noise and persistence rules keep it working all session under 40 lines.

This skill is the one-shot setup helper and is self-contained: both installable templates ship in `assets/`.

## Install steps

1. Ask the user: repo-level or global?
2. Repo-level: copy the template next to this file to the project root as `AGENTS.md` — `assets/AGENTS.md` for Chinese sessions, `assets/AGENTS.en.md` for English sessions.
   Global: same content into the user-level instructions file — `~/.zcode/AGENTS.md` (ZCode) or `~/.claude/CLAUDE.md` (Claude Code).
3. If the target file already exists, merge the "Turn discipline", "Capability menu" and "Hard rules" sections into it; never overwrite the whole file.
4. Verify: tell the user to start a NEW session and say "menu" (or 菜单). The capability table coming back means the install worked.
5. Offer to register their first real capability in the menu table — one row: number, trigger phrase, what it does, pointer to details.
