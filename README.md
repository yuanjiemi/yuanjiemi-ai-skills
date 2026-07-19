# 元解密 AI Skills

这里收录面向真实内容运营场景、可以由 AI 智能体直接使用的 Skills。

## 已有 Skills

| Skill | 作用 | 是否依赖 n8n | 状态 |
|---|---|---|---|
| [公众号文章编辑](skills/wechat-article/) | 先选 CTA，再生成标题、正文和 CTA，审核后生成排版预览 | 否 | 第一版测试中 |

每个 Skill 都以独立目录保存，核心入口是目录中的 `SKILL.md`。复制或安装对应目录后，即可通过 `$skill-name` 显式调用；支持 Skills 的智能体也可以根据描述自动触发。

## 如何确认 Skill 已启用

自然语言触发后，`wechat-article` 会先显示：`已启用「公众号文章编辑」`。看到这行即可确认智能体加载了 Skill，而不是在自由写作。

- Codex 显式调用：`$wechat-article`
- Claude Code 显式调用：`/wechat-article`
- 自然语言调用：`把这个脚本改成公众号文章：链接`

## 安装

仓库公开后，可以把 `skills/wechat-article` 目录安装到不同智能体。

### Codex

在 Codex 中发送：

```text
请使用 $skill-installer 从 GitHub 仓库 yuanjiemi/yuanjiemi-ai-skills 安装 skills/wechat-article
```

安装后新建一个任务测试；如果没有立即出现，重启 Codex。

### Claude Code

个人安装目录为：

```text
~/.claude/skills/wechat-article/
```

项目内安装目录为：

```text
.claude/skills/wechat-article/
```

把完整的 `wechat-article` 文件夹复制到其中一个目录，不要只复制 `SKILL.md`，否则排版标准等引用文件会丢失。

本仓库暂不包含任何真实账号凭证、客户数据或生产系统配置。
