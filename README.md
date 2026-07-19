<div align="center">

# YUAN元解密 AI Skills

### AI工具不用追，系统要搭起来。

这里收录我在真实内容运营、个人品牌和一人公司场景中验证过的 Agent Skills。<br>
先安装一个小 Skill 跑通，再慢慢升级成自己的 AI 工作系统。

[🎁 免费领取完整 AI 系统搭建指南](https://learn.yuanjiemi.com/template) · [⬇️ 下载最新通用 Skill 包](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.5/wechat-article-skill-v1.0.5.zip)

</div>

---

## 🚀 已发布 Skills

| Skill | 它能帮你做什么 | 是否依赖 n8n | 状态 |
|---|---|---|---|
| [根据视频脚本生成公众号文案 Skill](skills/wechat-article/) | 先选 CTA，再生成标题、正文和 CTA，审核后生成排版预览 | 否 | v1.0.5 已发布 |
| [公众号对标文章采集与分析 Skill](skills/wechat-benchmark-research/) | 单篇文章直接拆解；配置世界树 API 后，可采集指定账号最新 3 篇并批量写入本地 Excel | 否 | v1.0.0 已发布 |

每个 Skill 都以独立目录保存，核心入口是目录中的 `SKILL.md`。安装时必须保留完整文件夹，不能只复制 `SKILL.md`，否则写作和排版标准会丢失。

### 公众号对标文章采集与分析 Skill

> 指定对标账号 → 采集最新 3 篇 → 按原表 21 个字段拆解 → 原文链接去重 → 保存本地 Excel → 生成选题

这个 Skill 不依赖 n8n，也不要求飞书 App ID 或机器人。它有两种模式：

- 模板字段与元解密现有飞书多维表格保持一致：研究库 21 个字段、对标源库 6 个字段。
- **单篇免费模式**：用户发送文章链接、正文或截图即可拆解，不需要配置 API。
- **账号采集模式**：用户在自己电脑的私有配置文件中填写世界树 API Key；每个新账号首次提供任意一篇文章链接，以后只需说“采集这个账号最新 3 篇”。
- API Key 不进入 GitHub、Excel 或聊天记录；实际配置默认保存在用户自己的系统配置目录。
- 需要云端查看时，可把生成的 Excel 手动导入飞书、Notion 或 Google Sheets。
- 当前版不执行定时采集，不自动登录或发布公众号文章。

[下载公众号对标研究库 Excel 模板](skills/wechat-benchmark-research/assets/公众号对标灵感库模板.xlsx)

#### 第一次使用：申请自己的世界树 API Key

> [!IMPORTANT]
> 公开 Skill 不包含、也不会共用元子的世界树 Key。只有“按账号采集最新 3 篇”需要第三方 API；单篇文章拆解不需要 Key。

1. 打开[世界树官网](https://www.worldtreetech.cn/)，联系服务方申请自己的 API Key，并确认当前额度和计费规则。
2. 安装 Skill 后第一次运行账号采集，它会自动创建本机私有配置，并显示具体文件位置。
3. 用户只在自己电脑的配置文件中填写 Key，然后回复“已经配置好”。不要把 Key 发进聊天框、截图或 GitHub。
4. 暂时不想申请 Key，可以直接提供单篇文章正文、完整截图或可访问链接，继续使用免费拆解与 Excel 入库功能。

[查看世界树接口文档](https://s.apifox.cn/2592d2ef-25b9-4e40-b92b-c1484ee35b14)

#### 安装与测试

[下载完整通用 Skill 包](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/wechat-benchmark-v1.0.0/wechat-benchmark-research-skill-v1.0.0.zip)

在 Codex 中直接发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-benchmark-research
```

安装后新建任务，可以这样测试：

```text
采集“公众号名称”最新3篇文章并收进对标研究库
```

正常情况下，第一行会显示：

```text
已启用「公众号对标文章采集与分析 Skill」
```

其他支持 `SKILL.md` 的智能体，可下载通用 ZIP，并把完整的 `wechat-benchmark-research` 文件夹安装到其 Skills 目录。安装时不能只复制 `SKILL.md`，否则配置脚本和 Excel 模板会缺失。

## ✨ 它是怎么工作的？

> 视频脚本 → 选择默认或自定义 CTA → 生成 5 个标题和正文 → 按反馈局部修改 → 生成微信公众号排版预览

它适合不懂 n8n、但想先把“视频脚本转公众号文章”这个小流程跑通的人。它不会自动登录公众号、上传草稿或采集发布数据；这些功能需要使用[进阶版公众号 n8n 工作流](https://github.com/yuanjiemi/yuanjiemi-n8n-templates)。

### v1.0.5 更新

- 视频承接型正文默认使用更适合手机阅读的短段落。
- 生成排版预览时保留已经审核的标题、正文和段落边界。
- 默认 CTA 保留原有短段落，并固定扫码提示、模板库名称和预约文字的强调样式。
- 默认领取文案统一为“添加元子微信”。

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

[下载最新版 `wechat-article-skill-v1.0.5.zip`](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.5/wechat-article-skill-v1.0.5.zip)

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
