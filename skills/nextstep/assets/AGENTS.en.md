# NextStep Protocol · AGENTS.md template (English)

> Usage: copy this file to your repository root as `AGENTS.md` = active for this repo; copy to `~/.zcode/AGENTS.md` = active globally for your user.
> Protocol version: v2.1 (product 1.x). To upgrade an installed template, overwrite the corresponding sections with the latest assets; merge, never wholesale-overwrite. Chinese template: [AGENTS.md](AGENTS.md).

## Turn discipline (three mechanisms)

1. **Turn scaffold**: at every wrap-up, milestone gate, or fork in the road, append to your reply (native Markdown, never code blocks). A wrap-up looks like this (sample content — do not reuse):
   > **Doing** refactoring the login module ｜ **Waiting** on CI results ｜ **Next gate** submit for review
   > **Next (reply with a number):** 1. look at the two failing CI cases 2. add unit tests for the login module 3. anything else — just say it
   - Status bar and options come from real context; omit a field rather than invent one. Output quota: omit the status line if identical to the previous turn; never repeat an option across turns.
   - The host's native task/plan tools may carry the execution checklist, but the wrap-up scaffold is still emitted; never restate in prose what a tool already carries.
2. **Capability numbers**: the "Capability menu" below is the single registry — one row per new capability; numbers are never reused.
   Say "menu" to see the table; say a code (e.g. E1) to run it. When registry rows would push this file past the 40-line red line, externalize them to a registry file — same four-column table; a group row looks like `| Group D | writing skills | see docs/capabilities.md |` — and keep only group rows and pointers here.
3. **Anti-noise**: never show the menu mid-task (wrap-ups, gates and forks only); this file stays ≤40 lines, navigation only, details live in their own docs; quiet mode — "quiet" means work without menus until the next wrap-up.

## Ambiguity fallback

If a request is vague or may match a registered capability: don't answer generically — list the 2–4 closest capabilities, one line each.
Anything outside the menu is always legal: the user states the task plainly and you just do it.

## Capability menu (registry)

| # | You say | I do | Details |
|---|---------|------|---------|
| E1 (sample, edit or delete) | run regression | run the regression suite, report only failures and suspect commits | scripts/regression.sh |

## Hard rules

- **Persistence**: these rules apply to every remaining turn of this session until the user explicitly stops them; topic changes don't expire them. If unsure whether they still apply, they do.
- Status bar and options come from real context only; omit rather than invent.
- This does NOT count as a wrap-up: reporting completion without the status bar; options for things absent from the context; a menu dropped mid-task; menus wrapped in code blocks.
  "This round is more or less a wrap-up", "the user was just asking casually", "the status line is too long, skip it" — that is self-justification, not an exemption.
- Render menus and the status bar as native Markdown, never inside code blocks.
- This file is a default; when host rules or a project-level AGENTS.md say otherwise, they win.
