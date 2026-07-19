<div align="center">

# YUAN元解密 AI Skills

### AI工具不用追，系统要搭起来。

这里收录我在真实内容运营、个人品牌和一人公司场景中验证过的 Agent Skills。<br>
先安装一个小 Skill 跑通，再慢慢升级成自己的 AI 工作系统。

[🎁 免费领取完整 AI 系统搭建指南](https://learn.yuanjiemi.com/template) · [⬇️ 下载最新通用 Skill 包](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.4/wechat-article-skill-v1.0.4.zip)

</div>

---

## 🚀 已发布 Skills

| Skill | 它能帮你做什么 | 是否依赖 n8n | 状态 |
|---|---|---|---|
| [根据视频脚本生成公众号文案 Skill](skills/wechat-article/) | 先选 CTA，再生成标题、正文和 CTA，审核后生成排版预览 | 否 | v1.0.4 已发布 |

每个 Skill 都以独立目录保存，核心入口是目录中的 `SKILL.md`。安装时必须保留完整文件夹，不能只复制 `SKILL.md`，否则写作和排版标准会丢失。

## ✨ 它是怎么工作的？

> 视频脚本 → 选择默认或自定义 CTA → 生成 5 个标题和正文 → 按反馈局部修改 → 生成微信公众号排版预览

它适合不懂 n8n、但想先把“视频脚本转公众号文章”这个小流程跑通的人。它不会自动登录公众号、上传草稿或采集发布数据；这些功能需要使用[进阶版公众号 n8n 工作流](https://github.com/yuanjiemi/yuanjiemi-n8n-templates)。

## ✅ 如何确认 Skill 已启用

新开一个任务，直接发送：

```text
把这个脚本改成公众号文章：你的脚本或链接
```

正常情况下，第一行会显示：

```text
已启用「根据视频脚本生成公众号文案 Skill」
```

看到这行，即可确认智能体加载了 Skill，而不是在自由写作。

- Codex 显式调用：`$wechat-article`
- Claude Code 显式调用：`/wechat-article`
- 自然语言调用：`把这个脚本改成公众号文章：链接`

> [!NOTE]
> 公开安装包自带元子的“AI 提效模板库”默认 CTA 文案和公开领取图片。你也可以提供自己的 CTA 文案或文档链接，或者回复“本次不加 CTA”。安装包不包含公众号 AppID、Secret、Webhook、飞书表格 ID 等账号配置或密钥。

## 📦 安装

### 通用安装包

[下载最新版 `wechat-article-skill-v1.0.4.zip`](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.4/wechat-article-skill-v1.0.4.zip)

这是完整的通用 Skill 包：可以上传到 WorkBuddy，也可以解压后安装到 Claude Code、OpenClaw 或其他支持 `SKILL.md` 的智能体。

### Codex

在 Codex 中发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-article
```

安装后新建一个任务测试；如果没有立即出现，重启 Codex。

### Claude Code

下载并解压通用安装包，然后把完整的 `wechat-article` 文件夹复制到其中一个目录：

```text
# 个人全局安装
~/.claude/skills/wechat-article/

# 当前项目安装
.claude/skills/wechat-article/
```

复制完成后重启 Claude Code。

### WorkBuddy

1. 下载上面的通用 Skill ZIP。
2. 打开 WorkBuddy 的“技能”页面。
3. 选择“添加技能”→“上传技能”，上传 ZIP。
4. 确认“根据视频脚本生成公众号文案 Skill”已启用，再新建任务测试。

WorkBuddy 官方说明：[Skills 市场与本地技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

### OpenClaw（开源小龙虾）

> [!IMPORTANT]
> 下面整段命令只能粘贴到运行 OpenClaw Gateway 的电脑或服务器的**系统终端 Terminal**，不要发送给“小龙虾”聊天框。聊天代理可能被 `PreToolUse hook` 拦截，这不代表仓库或 Skill 有问题。

在系统终端中一次性粘贴下面整段。它可以重复执行：仓库不存在就下载，已经存在就更新，然后强制安装最新版 Skill。

```bash
cd "$HOME"
if [ -d "$HOME/yuanjiemi-ai-skills/.git" ]; then
  git -C "$HOME/yuanjiemi-ai-skills" pull
else
  git clone https://github.com/yuanjiemi/yuanjiemi-ai-skills.git "$HOME/yuanjiemi-ai-skills"
fi
openclaw skills install "$HOME/yuanjiemi-ai-skills/skills/wechat-article" --as wechat-article --global --force
```

> [!NOTE]
> 删除 `~/.openclaw/skills/wechat-article` 只代表删除了已安装的 Skill，不会自动删除 `$HOME/yuanjiemi-ai-skills` Git 仓库。因此重复安装时不能直接再次运行原来的 `git clone`，上面的命令会自动判断并改用 `git pull`。

如果命令安装仍不可用，可以手动安装：

1. 下载并解压上面的通用 Skill ZIP。
2. 把完整的 `wechat-article` 文件夹放进 `~/.openclaw/skills/`。
3. 确认最终文件是 `~/.openclaw/skills/wechat-article/SKILL.md`，并且 `skills` 目录中没有另一个旧版同名 Skill。
4. 完全新开一个 OpenClaw 会话，再发送测试指令。

OpenClaw 官方说明：[Skills 安装与加载目录](https://docs.openclaw.ai/tools/skills)。

### 其他智能体

只要智能体支持 Agent Skills / `SKILL.md`，通常都可以把完整文件夹安装到它规定的 Skills 目录。普通网页聊天机器人如果没有 Skills 功能，不能真正安装；只能把 `SKILL.md` 作为项目说明或系统指令使用。

---

## 🔹更多模版库

这个资料库就是我用这套方法，持续整理出来的 AI 系统实战手册。它不是一次性看完的东西——你可以在不同阶段回来，找到适合自己的那一层。

➡️ [从工具焦虑到系统自由：AI 系统搭建指南](https://learn.yuanjiemi.com/template)

里面会持续更新：

- 真实场景中验证过的 Agent Skills
- n8n 工作流与配置教程
- 视频配套资料和可下载附件
- AI 系统搭建案例、清单和复盘方法

## 🔹关于元子

我在世界 500 强做了 7 年财务分析和业务控制，读完了复旦 FMBA，也拿了 ACCA、CMA 和 PMP 三张证书。

以前我看生意，习惯先看目标、流程、成本、结果和 ROI。现在我看 AI 工具，用的也是同一套方法：它到底解决什么问题？能省多少时间和成本？值不值得放进一个固定工作流里长期复用？

我越来越相信，普通人不需要追每一个 AI 热点，而是要把合适的工具放进自己的内容、运营、成本、交付和学习系统里。

## 🔹你可以在哪里找到我

![联系元子：微信、Line与公众号](assets/contact-yuanzi.png)

- 全平台：`@YUAN元解密`
- [YouTube](https://www.youtube.com/@yuanzixuejie)
- [B站](https://space.bilibili.com/44402512)
- [Line](https://line.me/R/ti/p/@958nmzlj?oat_content=url)
- [添加元子微信](https://hi.yuanjiemi.com/yuan)
- 视频号、公众号：搜索「YUAN元的进阶笔记」

---

## 使用说明

欢迎个人学习和使用；未经授权，请勿打包售卖、冒充原创或移除来源说明。

本仓库不包含任何真实账号凭证、客户数据或生产系统配置。
