# 元解密 AI Skills

AI工具不用追，系统要搭起来。

这里收录我在真实内容运营、个人品牌和一人公司场景中验证过的 Agent Skills。你可以先安装一个小 Skill 跑通，再慢慢升级成自己的 AI 工作系统。

想要更多真实场景的 Skills、n8n 模板、视频配套资料和搭建指南？

👉 [免费领取《从工具焦虑到系统自由：AI系统搭建指南》](https://learn.yuanjiemi.com/template)

## 已有 Skills

| Skill | 作用 | 是否依赖 n8n | 状态 |
|---|---|---|---|
| [根据视频脚本生成公众号文案 Skill](skills/wechat-article/) | 先选 CTA，再生成标题、正文和 CTA，审核后生成排版预览 | 否 | v1.0.1 已发布 |

每个 Skill 都以独立目录保存，核心入口是目录中的 `SKILL.md`。复制或安装对应目录后，即可通过 `$skill-name` 显式调用；支持 Skills 的智能体也可以根据描述自动触发。

## 如何确认 Skill 已启用

自然语言触发后，`wechat-article` 会先显示：`已启用「根据视频脚本生成公众号文案 Skill」`。看到这行即可确认智能体加载了 Skill，而不是在自由写作。

- Codex 显式调用：`$wechat-article`
- Claude Code 显式调用：`/wechat-article`
- 自然语言调用：`把这个脚本改成公众号文章：链接`

## 安装

安装时必须保留完整的 `wechat-article` 文件夹，不能只复制 `SKILL.md`，否则写作和排版标准会丢失。

### 通用安装包

[下载最新版 `wechat-article-skill-v1.0.1.zip`](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.1/wechat-article-skill-v1.0.1.zip)

这是完整的通用 Skill 包：可以直接上传到 WorkBuddy，也可以解压后安装到 Claude Code、OpenClaw 或其他支持 `SKILL.md` 的智能体。Codex 用户建议使用下面的一键安装方式。

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

1. 下载上面的通用 Skill ZIP。
2. 打开 WorkBuddy 的“技能”页面。
3. 选择“添加技能”→“上传技能”，上传 ZIP。
4. 确认“根据视频脚本生成公众号文案 Skill”已启用，再新建任务测试。

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

正常情况下，智能体会先显示 `已启用「根据视频脚本生成公众号文案 Skill」`，然后询问使用默认 CTA 还是自定义 CTA。

公开安装包不会携带元子的私人 CTA、二维码或账号配置。首次使用时，如果当前智能体没有可读取的默认 CTA，请提供自己的 CTA 文案或文档链接；也可以回复“本次不加 CTA”。

## 更多免费资源

### 免费领取完整 AI 系统搭建指南

这个 Skill 只是其中一个小场景。我还会持续整理真实场景中验证过的 Skills、n8n 工作流、视频配套资料、模板、案例和搭建思路。

👉 [免费领取《从工具焦虑到系统自由：AI系统搭建指南》](https://learn.yuanjiemi.com/template)

### 关于元子

我在世界 500 强做了 7 年财务分析和业务控制，读完了复旦 FMBA，也拿了 ACCA、CMA 和 PMP 三张证书。

以前我看生意，习惯先看目标、流程、成本、结果和 ROI。现在我看 AI 工具，用的也是同一套方法：它到底解决什么问题？能省多少时间和成本？值不值得放进一个固定工作流里长期复用？

我越来越相信，普通人不需要追每一个 AI 热点，而是要把合适的工具放进自己的内容、运营、成本、交付和学习系统里。

### 你可以在哪里找到我

- 全平台：`@YUAN元解密`
- [YouTube](https://www.youtube.com/@yuanzixuejie)
- [B站](https://space.bilibili.com/44402512)
- [Line](https://line.me/R/ti/p/@958nmzlj?oat_content=url)
- [添加元子微信](https://hi.yuanjiemi.com/yuan)
- 视频号、公众号：搜索「YUAN元的进阶笔记」

## 使用说明

欢迎个人学习和使用；未经授权，请勿打包售卖、冒充原创或移除来源说明。

本仓库暂不包含任何真实账号凭证、客户数据或生产系统配置。
