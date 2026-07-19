# 元解密 AI Skills

这里收录面向真实内容运营场景、可以由 AI 智能体直接使用的 Skills。

## 已有 Skills

| Skill | 作用 | 是否依赖 n8n | 状态 |
|---|---|---|---|
| [公众号文章编辑](skills/wechat-article/) | 先选 CTA，再生成标题、正文和 CTA，审核后生成排版预览 | 否 | v1.0 已发布 |

每个 Skill 都以独立目录保存，核心入口是目录中的 `SKILL.md`。复制或安装对应目录后，即可通过 `$skill-name` 显式调用；支持 Skills 的智能体也可以根据描述自动触发。

## 如何确认 Skill 已启用

自然语言触发后，`wechat-article` 会先显示：`已启用「公众号文章编辑」`。看到这行即可确认智能体加载了 Skill，而不是在自由写作。

- Codex 显式调用：`$wechat-article`
- Claude Code 显式调用：`/wechat-article`
- 自然语言调用：`把这个脚本改成公众号文章：链接`

## 安装

安装时必须保留完整的 `wechat-article` 文件夹，不能只复制 `SKILL.md`，否则写作和排版标准会丢失。

### Codex

在 Codex 中发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-article
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

把完整的 `wechat-article` 文件夹复制到其中一个目录，然后重启 Claude Code。

### WorkBuddy

1. 在本仓库的 Releases 页面下载 `wechat-article-v1.0.0.zip`。
2. 打开 WorkBuddy 的“技能”页面。
3. 选择“添加技能”→“上传技能”，上传 ZIP。
4. 确认“公众号文章编辑”已启用，再新建任务测试。

WorkBuddy 官方说明：[Skills 市场与本地技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

### OpenClaw（开源小龙虾）

先克隆仓库，再安装 Skill：

```bash
git clone https://github.com/yuanjiemi/yuanjiemi-ai-skills.git
openclaw skills install ./yuanjiemi-ai-skills/skills/wechat-article --as wechat-article --global
```

OpenClaw 官方说明：[Skills](https://docs.openclaw.ai/tools/skills)。

### 其他智能体

只要智能体支持 Agent Skills / `SKILL.md`，通常都可以把完整文件夹安装到它规定的 Skills 目录。普通网页聊天机器人如果没有 Skills 功能，不能真正安装；只能把 `SKILL.md` 作为项目说明或系统指令使用。

## 安装后测试

新开一个任务，直接发送：

```text
把这个脚本改成公众号文章：你的脚本或链接
```

正常情况下，智能体会先显示 `已启用「公众号文章编辑」`，然后询问使用默认 CTA 还是自定义 CTA。

## 使用说明

欢迎个人学习和使用；未经授权，请勿打包售卖、冒充原创或移除来源说明。

本仓库暂不包含任何真实账号凭证、客户数据或生产系统配置。
