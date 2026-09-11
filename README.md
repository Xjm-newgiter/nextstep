# NextStep

> Options handed to you. Reply with a number to move forward.
> A resident `AGENTS.md` protocol that gives every AI coding session a "what's next", and turns your team's scripts and workflows into numbered, zero-memory commands.

English · [简体中文](README.zh-CN.md)

Works with any AI coding assistant that reads `AGENTS.md`: ZCode, Claude Code, Codex, Cursor, and more.

## The problem

- Your agent finishes a task and stops. *What's next?* is always your job.
- The scripts, workflows and conventions your team built have trigger words nobody remembers.
- Stuffing prompt lists to fix the two problems above backfires: the longer the list, the worse the model performs.

## What it does

Three mechanisms, ≤40 lines of `AGENTS.md`, no dependencies:

1. **Turn scaffold** — at every wrap-up the assistant appends a one-line status bar (Doing / Waiting / Next gate) and up to 5 numbered next steps drawn from real context. Reply with a number; it runs; wrap up; repeat.
2. **Capability numbers** — a registry table maps numbers to capabilities. Say "menu" to see all of them, say a code like `E1` to run one. A new capability costs one new row.
3. **Anti-noise** — no menus mid-task; say "quiet" and it works silently until the next wrap-up.

Anything outside the menu is always allowed: just say what you want.

## What changes

| Before | After |
|--------|-------|
| Agent finishes, goes silent, you type "what now?" | Every wrap-up ends with a status bar and numbered next steps. |
| "What was that deploy script called again?" | You type `D2`. The registry remembers so you don't have to. |
| A 200-line prompt file the model only half-reads. | ≤40 lines, navigation only; details live where they're used. |

## Install

**Per repo** — copy [`skills/nextstep/assets/AGENTS.md`](skills/nextstep/assets/AGENTS.md) (Chinese sessions) or [`skills/nextstep/assets/AGENTS.en.md`](skills/nextstep/assets/AGENTS.en.md) (English sessions) to your repository root as `AGENTS.md`.

**Global / personal** — same content into your user-level instructions file: `~/.zcode/AGENTS.md` (ZCode) or `~/.claude/CLAUDE.md` (Claude Code).

If the target file already exists, merge sections instead of overwriting.

**As a skill** (one-shot setup helper, shipped self-contained with both templates):

```bash
npx skills add Xjm-newgiter/nextstep@nextstep --global
```

**As a ZCode plugin** — in ZCode: Create → Add marketplace → `https://github.com/Xjm-newgiter/nextstep`, then install `nextstep`. Claude Code: `/plugin marketplace add Xjm-newgiter/nextstep` then `/plugin install nextstep@nextstep`.

> Gitee mirror: gitee.com/xujingmeng/nextstep. The skills CLI shorthand above targets GitHub; Gitee users should clone and copy the template manually.

## Verify

Start a new session and say "menu". If the assistant answers with the capability table, it's live.

## FAQ

**How is this different from a skill or a subagent?**
It's neither. A skill is a manual loaded on demand; a subagent is a worker with its own context window. NextStep is standing house rules, read automatically in every session. The three compose fine.

**Won't the menus make everything noisier?**
The protocol polices itself: menus only at wrap-ups and gates, the file itself stays ≤40 lines, and "quiet" switches to silent mode.

**Where do I register capabilities?**
In the "Capability menu" table inside your `AGENTS.md`. One row each: number, trigger phrase, what it does, pointer to details. Past 8 rows, externalize the registry to a file and keep group rows and pointers in `AGENTS.md`.

**Is the spec available in English?**
Not yet — the full spec (会话推进协议.md) is Chinese-only for now. Both AGENTS.md templates are fully self-contained in their language, so this only affects reference reading. Tracked in [docs/open-questions.md](docs/open-questions.md).

**When does the installer skill NOT run?**
By design, only install/manage requests wake it. It stays dormant when: the protocol is already installed (daily "menu" and number replies run via AGENTS.md, not the skill); the session started before installation; a same-named skill shadows it at a higher-precedence path (`~/.zcode/skills` > `~/.agents/skills` > project > plugin); it's disabled in client settings; the request doesn't match the description (fixing bugs, writing code); or the frontmatter fails to parse. The skill not running never means the protocol stopped working.

## License

[MIT](LICENSE)
