# 根据视频脚本生成公众号文案 Skill

[← 返回全部 Skills](../../README.md)

把中文视频口播稿、字幕稿、提纲或已有草稿，编辑成适合微信公众号阅读和承接视频流量的文章。

> 视频脚本 → 选择默认或自定义 CTA → 生成 5 个标题、正文和 CTA → 根据反馈修改 → 生成排版预览

## 它能帮你做什么

- 一次提供 5 个标题，并推荐一个优先标题。
- 把视频表达改成适合手机阅读的公众号短段落。
- 使用元子的默认 CTA、自定义 CTA，或本次不加 CTA。
- 用户确认内容后生成带颜色、强调和二维码位置的 HTML 排版预览。
- 保留视频事实边界，不擅自补造案例、成绩或观点。

## 最简单的使用方式

安装后新建任务，直接说：

```text
把这个脚本改成公众号文章：脚本或链接
```

正常情况下，第一行会显示：

```text
已启用「根据视频脚本生成公众号文案 Skill」
```

不需要记住英文 Skill 名称。Codex 也支持显式调用：`$wechat-article`。

## 下载

[下载完整通用 Skill 包 v1.0.5](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/v1.0.5/wechat-article-skill-v1.0.5.zip)

通用 ZIP 可用于 WorkBuddy，也可解压后安装到 Claude Code、OpenClaw 或其他支持 `SKILL.md` 的智能体。

## 安装

### Codex

在 Codex 中发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-article
```

安装后新建任务测试；如果没有立即出现，重启 Codex。

### Claude Code

下载并解压通用 ZIP，把完整的 `wechat-article` 文件夹复制到其中一个目录：

```text
# 个人全局安装
~/.claude/skills/wechat-article/

# 当前项目安装
.claude/skills/wechat-article/
```

复制完成后重启 Claude Code。

### WorkBuddy

1. 下载通用 ZIP。
2. 打开 WorkBuddy 的“技能”页面。
3. 选择“添加技能”→“上传技能”，上传 ZIP。
4. 确认“根据视频脚本生成公众号文案 Skill”已启用，再新建任务测试。

### OpenClaw

下面的命令要粘贴到运行 OpenClaw Gateway 的电脑或服务器的系统终端，不要发送到聊天框：

```bash
cd "$HOME"
if [ -d "$HOME/yuanjiemi-ai-skills/.git" ]; then
  git -C "$HOME/yuanjiemi-ai-skills" pull
else
  git clone https://github.com/yuanjiemi/yuanjiemi-ai-skills.git "$HOME/yuanjiemi-ai-skills"
fi
openclaw skills install "$HOME/yuanjiemi-ai-skills/skills/wechat-article" --as wechat-article --global --force
```

如果命令安装不可用，也可以解压通用 ZIP，把完整文件夹放到 `~/.openclaw/skills/wechat-article/`，确认其中直接包含 `SKILL.md`，再新开会话。

### 其他智能体

只要支持 Agent Skills / `SKILL.md`，就可以把完整文件夹安装到它规定的 Skills 目录。普通网页聊天机器人如果不支持 Skills，只能把 `SKILL.md` 作为项目指令，不能真正安装。

## 默认 CTA 与安全边界

公开安装包自带元子的“AI 提效模板库”默认 CTA 文案和公开领取图片。用户也可以提供自己的 CTA，或回复“本次不加 CTA”。

安装包不包含公众号 AppID、Secret、Webhook、飞书表格 ID 或其他账号密钥。本 Skill 不登录公众号后台，也不负责自动上传草稿和发布文章。

需要自动上传和发布回填时，可使用[进阶版公众号 n8n 工作流](https://github.com/yuanjiemi/yuanjiemi-n8n-templates)。

## v1.0.5 更新

- 视频承接型正文默认使用更适合手机阅读的短段落。
- 排版预览保留已经审核的标题、正文和段落边界。
- 默认 CTA 固定扫码提示、模板库名称和预约文字的强调样式。
- 默认领取文案统一为“添加元子微信”。

---

## 🔹更多模版库

这个资料库是我持续更新的 AI 系统实战手册。它不是一次性看完的东西——你可以在不同阶段回来，找到适合自己的那一层。

➡️ [免费领取《从工具焦虑到系统自由：AI 系统搭建指南》](https://learn.yuanjiemi.com/template)

里面会持续更新：

- 真实场景中验证过的 Agent Skills
- n8n 工作流与配置教程
- 视频配套资料和可下载附件
- AI 系统搭建案例、清单和复盘方法

## 🔹关于元子

我在世界 500 强做了 7 年财务分析和业务控制，读完复旦 FMBA，也拿了 ACCA、CMA 和 PMP 三张证书。

以前我看生意，习惯先看目标、流程、成本、结果和 ROI。现在我看 AI 工具，用的也是同一套方法：它解决什么问题？能省多少时间和成本？值不值得进入一个固定工作流长期复用？

## 🔹联系元子

![联系元子：微信、Line与公众号](../../assets/contact-yuanzi.png)

- 全平台：`@YUAN元解密`
- [YouTube](https://www.youtube.com/@yuanzixuejie)
- [B站](https://space.bilibili.com/44402512)
- [Line](https://line.me/R/ti/p/@958nmzlj?oat_content=url)
- [添加元子微信](https://hi.yuanjiemi.com/yuan)
- 视频号、公众号：搜索「YUAN元的进阶笔记」
