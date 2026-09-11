# NextStep · 会话推进协议

> 选项递到眼前，回一个数字就能推进。
> 给 AI 编码助手装一套"零记忆"的推进方式：每轮收口自动给出下一步，沉淀的能力说编号就能调。

[English](README.md) · 简体中文

适用于 ZCode / Claude Code / Codex / Cursor 等任何自动读取 `AGENTS.md` 的 AI 编码助手。

## 解决什么问题

- AI 干完一件事就停下，"接下来干嘛"永远要你自己想；
- 团队沉淀的脚本、流程、规范，触发词没人记得住；
- 往提示词里堆清单来救，可清单越长模型表现越差。

## 三个机制

| 机制 | 一句话 | 细节 |
|------|--------|------|
| 回合脚手架 | 每次收口附状态栏 1 行 + 「下一步」编号选项 ≤5，回数字即执行，循环推进 | 《会话推进协议.md》§三 |
| 能力编号 | 能力登记成表；说「菜单」看全表，说编号（如 B1）直接调用 | 同上 |
| 防噪三纪律 | 执行中途不出菜单、文件保持 ≤40 行只做导航、说「安静」即静默 | 同上 |

菜单外的事永远合法：直接说正事，AI 直接干。

## 长什么样

一轮工作收口时，AI 回复的末尾会长这样：

> **在办** 重构登录模块 ｜ **在途** 等 CI 结果 ｜ **下一闸口** 提交评审
>
> **下一步（回数字即可）：**
>
> 1. 先看 CI 挂掉的两条用例
> 2. 补登录模块的单元测试
> 3. 其他 —— 直接说事，不受限

回个数字它就接着干；想干别的直接说，永远不受限。

## 安装（多选一）

- 单仓库生效：把 [`skills/nextstep/assets/AGENTS.md`](skills/nextstep/assets/AGENTS.md)（中文会话）或 [`skills/nextstep/assets/AGENTS.en.md`](skills/nextstep/assets/AGENTS.en.md)（英文会话）复制到仓库根 `AGENTS.md`；
- 个人全局生效：同内容复制到用户级指令文件，如 `~/.zcode/AGENTS.md`（ZCode）、`~/.claude/CLAUDE.md`（Claude Code）。

目标位置已有 AGENTS.md 时追加合并，不要覆盖。模板头部标注协议版本——升级已装模板＝用最新 `skills/nextstep/assets/` 模板覆盖对应区段（合并原则不变）。

也可以装成技能，让技能代劳安装：

```bash
npx skills add Xjm-newgiter/nextstep@nextstep --global
```

ZCode 插件方式：Create → Add marketplace → 填 `https://github.com/Xjm-newgiter/nextstep`，然后安装 `nextstep`。Claude Code：`/plugin marketplace add Xjm-newgiter/nextstep` 后 `/plugin install nextstep@nextstep`。

> Gitee 镜像：gitee.com/xujingmeng/nextstep。上面 skills 命令的简写形式指向 GitHub，Gitee 用户请克隆后手动复制模板。

## 验证

新开会话说「菜单」，AI 回出能力表 = 安装成功。

## 常见问题

**和 skill、subagent 什么关系？**
都不是。Skill 是按需加载的操作手册，subagent 是派出去干活的分身，NextStep 是每次会话自动生效的推进规矩，写在 `AGENTS.md` 里。三者互不冲突，可以同时用。

**会不会把对话搞得很啰嗦？**
协议自带防噪：只在收口、闸口、分叉处出菜单；文件本身 ≤40 行；说「安静」就进入静默模式，只干活不递菜单。

**能力登记在哪里？**
就登记在 AGENTS.md 的「能力菜单」表里，一行一个：编号、你说什么、我做什么、详情指针。超过 8 行时外置成登记文件，AGENTS.md 里只留分组行和指针。

**哪些情况安装技能不会运行？**
按设计，只有安装/管理协议的请求会唤醒它。以下情况不运行：协议已装好（日常「菜单」、回数字走 AGENTS.md，不经技能）；会话早于安装启动；同名技能在更高优先级路径遮蔽（`~/.zcode/skills` > `~/.agents/skills` > 项目级 > 插件）；客户端设置里被禁用；请求内容与描述不匹配（如修 bug、写代码）；frontmatter 解析错误。技能不运行 ≠ 协议不生效。

## License

[MIT](LICENSE)
