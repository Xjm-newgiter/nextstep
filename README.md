# NextStep

> Reply with a number and it moves.
> House rules for AI coding assistants. Paste them into `AGENTS.md` once, and every session follows them.

English · [简体中文](README.zh-CN.md)

Works with anything that reads `AGENTS.md`: ZCode, Claude Code, Codex, Cursor. It is text only, so there is nothing to install, nothing to phone home, and no dependencies to manage.

## The problem

An agent finishes a task and stops. Working out what comes next is your job again.

Your team's scripts and workflows have trigger words nobody remembers.

The usual fix is to pile more instructions into the prompt file. That makes the model follow them worse, not better.

## What it does

Three mechanisms, under 40 lines of `AGENTS.md`.

When a round of work ends, the assistant adds a status line and up to five numbered next steps taken from the actual conversation. You reply with a number, it does the thing, then it wraps up again.

A capability table maps numbers to capabilities. Say "menu" to see it, or say `E1` to run one. Adding a capability costs one row.

While work is in progress there are no menus at all. Say "quiet" and it stays quiet until the round ends. You can always ignore the table and just say what you want.

## What changes

| Before | After |
|--------|-------|
| Agent finishes, goes silent, you type "what now?" | Every round ends with a status line and numbered next steps. |
| "What was that deploy script called again?" | You type `D2`. The table remembers for you. |
| A 200-line prompt file the model half-reads. | Under 40 lines of navigation, with detail kept where it gets used. |

## What a round ending looks like

> **Doing** refactoring the login module ｜ **Waiting** on CI results ｜ **Next gate** submit for review
>
> **Next (reply with a number):**
> 1. look at the two failing CI cases
> 2. add unit tests for the login module
> 3. anything else, just say it

Reply with a number and it runs. Want something else? Say so.

## Install

Per repo: copy [`templates/AGENTS.md`](templates/AGENTS.md) for Chinese sessions, or [`templates/AGENTS.en.md`](templates/AGENTS.en.md) for English ones, to your repository root as `AGENTS.md`.

For your own machine instead: put the same content in your user-level instructions file, either `~/.zcode/AGENTS.md` (ZCode) or `~/.claude/CLAUDE.md` (Claude Code). Be aware this applies to every session in every workspace.

If the target file already exists, merge the sections rather than replacing the whole file. The template header carries a protocol version. To upgrade an installed template, overwrite the corresponding sections with the latest copy from `templates/`.

You can also let a skill do the setup:

```bash
npx skills add Xjm-newgiter/nextstep --global
```

> A Gitee mirror lives at gitee.com/xujingmeng/nextstep. The command above targets GitHub, so Gitee users should clone and copy the template by hand.

## Verify

Start a new session and say "menu". If the assistant answers with the capability table, it is live.

Then replace the E1 sample row with your first real capability. Numbers are never reused, so leaving E1 pointing at the placeholder burns that number for good.

## FAQ

**How is this different from a skill or a subagent?**
It is neither. A skill is a manual the agent loads on demand. A subagent is a worker with its own context window. NextStep is standing house rules, read automatically in every session. The three compose fine.

**How is this different from built-in task tools like TodoWrite or plan mode?**
Those carry execution state inside a turn, and only when the model reaches for them. NextStep adds a standing contract: the status line and numbered steps arrive at every round ending, in any host that reads `AGENTS.md`. It also brings the capability table and quiet mode. The two coexist, so native tools can hold the checklist while the status line still ships.

**Won't the menus get noisy?**
They are held to a budget. Menus appear only at round endings and gates, the file itself stays under 40 lines, and "quiet" switches them off until the next round ends.

**Where do capabilities get registered?**
In the capability table inside your `AGENTS.md`. One row each: number, trigger phrase, what it does, where the detail lives. When the table would push the file past 40 lines, move it to its own file and leave only group rows and pointers behind.

**What makes the skill go dormant?**
By design, only install and upgrade requests wake it. It stays dormant when the protocol is already installed (day to day, "menu" and number replies go through `AGENTS.md`, not the skill), when the session started before installation, when a same-named skill shadows it at a higher-precedence path, when it is disabled in client settings, when a request does not match its description such as fixing bugs or writing code, or when its frontmatter fails to parse. The skill not running never means the protocol stopped working.

**How do I turn it off or remove it?**
Say "stop the protocol" and the status line stops immediately, staying off until you ask to resume. To remove it for good, delete the three NextStep sections from your `AGENTS.md`: turn discipline, capability menu, hard rules. To remove the installer skill, uninstall it in your client's skill settings or delete its folder. Removal is easy on purpose, since the whole thing is text.

**I said "menu" and nothing happened.**
Work through these in order. Did you start a new session after installing? Does your `AGENTS.md` actually contain the turn discipline section? Does your host read the `AGENTS.md` at the path you edited? If you merged into an existing file, is the capability table still intact? And if your template header has no protocol version line, the install is an early build, so refresh it from the latest template.

**Is the spec available in English?**
Not yet. The full spec (`会话推进协议.md`) is Chinese only. Both templates are self-contained in their own language, so this only affects reference reading.

## License

[MIT](LICENSE)
