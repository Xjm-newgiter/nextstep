# NextStep Protocol · AGENTS.md template (English)

> Usage: copy this file to your repository root as `AGENTS.md` = active for this repo; copy to `~/.zcode/AGENTS.md` = active globally for your user.
> When the target file already exists, merge sections instead of overwriting. Chinese template: [AGENTS.md](AGENTS.md).

## Turn discipline (three mechanisms)

1. **Turn scaffold**: at every wrap-up, milestone gate, or fork in the road, append to your reply (native Markdown, never code blocks):
   - one status line: **Doing** … ｜ **Waiting** … ｜ **Next gate** … (drawn from real context; omit a field rather than invent one);
   - "Next (reply with a number):" up to 5 options drawn from real open items. A number runs the thing; then wrap up again.
   - Output quota: omit the status line if identical to the previous turn; never repeat an option across turns; prefer the host's native task/plan tools over restating plans in prose.
2. **Capability numbers**: the "Capability menu" below is the single registry — register every new capability as one row; numbers are never reused.
   The user says "menu" to see the table; says a code (e.g. E1) to run it. Past 8 rows, externalize the registry to a file (e.g. `docs/capabilities.md`) and keep only group rows and pointers here.
3. **Anti-noise**: never show the menu mid-task; stay thin (this file ≤40 lines, navigation only, details live in their own docs); quiet mode — when the user says "quiet", work without menus until the next wrap-up.

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
- This does NOT count as a wrap-up: reporting completion without the status bar; options for things absent from the context; a menu dropped mid-task.
- Render menus and the status bar as native Markdown, never inside code blocks.
- This file is a default; when host rules or a project-level AGENTS.md say otherwise, they win.
