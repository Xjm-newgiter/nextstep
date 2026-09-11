# NextStep Protocol · AGENTS.md template (English)

> Usage: copy this file to your repository root as `AGENTS.md` for this repo alone, or to `~/.zcode/AGENTS.md` for your whole machine.
> Protocol version: 1.0. To upgrade an installed template, overwrite the matching sections with the latest copy; merge, never wholesale-overwrite. Chinese template: [AGENTS.md](AGENTS.md).

## Turn discipline (three mechanisms)

1. **Turn scaffold**: at every round ending, milestone gate or fork in the road, append to your reply (native Markdown, never code blocks). A round ending looks like this (compact one-line form, semantically identical to the multi-line list in protocol §3; sample content, do not reuse):
   > **Doing** refactoring the login module ｜ **Waiting** on CI results ｜ **Next gate** submit for review
   > **Next (reply with a number):** 1. look at the two failing CI cases 2. add unit tests for the login module 3. anything else, just say it
   - Status line and options come from real context. Omit a field rather than invent one. Output quota: drop the status line if it matches the previous round, and never repeat an option across rounds.
   - The host's native task or plan tools may carry the execution checklist, but the wrap-up scaffold still ships. Do not restate in prose what a tool already carries.
2. **Capability numbers**: the capability menu below is the single registry. One row per new capability, and numbers are never reused. Say "menu" to see the table, say a code such as E1 to run it.
   When registry rows would push this file past the 40-line red line, externalize them to a registry file. Use the same four-column table, with group rows occupying a full row, for example `| Group D | writing | writing workflows registered there | docs/capabilities.md |`. Keep only group rows and pointers here.
3. **Anti-noise**: never show the menu mid-task, only at round endings, gates and forks. This file stays under 40 lines, navigation only, with details in their own docs. Quiet mode: "quiet" means work without menus until the next round ending.

## Ambiguity fallback

When a request is vague or may match a registered capability, do not answer generically. List the 2 to 4 closest capabilities, one line each, and let the user pick.
Anything outside the menu is always legal. The user states the task plainly and you just do it.

## Capability menu (registry)

| # | You say | I do | Details |
|---|---------|------|---------|
| E1 (sample, edit or delete) | run regression | run the regression suite, report only failures and suspect commits | scripts/regression.sh |

## Hard rules

- **Persistence**: these rules apply to every remaining round of this session until the user explicitly stops them. The stop phrase is "stop the protocol", which silences the scaffold until the user asks to resume. Topic changes do not expire them. If unsure whether they still apply, they do.
- Status line and options come from real context only. Omit rather than invent.
- This does not count as a round ending: reporting completion without the status line, options for things absent from the context, a menu dropped mid-task, or menus wrapped in code blocks.
  "This round is more or less wrapped up", "the user was just asking casually", "the status line is too long, skip it" are all self-justification, not an exemption.
- Render menus and the status line as native Markdown, never inside code blocks.
- This file is a default. When host rules or a project-level AGENTS.md say otherwise, they win.
