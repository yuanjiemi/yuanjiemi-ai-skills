# 公众号数据复盘 Skill

[← 返回全部 Skills](../../README.md)

把公众号后台截图、Excel、手动数字或文章链接，整理成能指导下一篇内容的复盘记录。

> 读取数据 → 计算互动 → 对比历史基准 → 连接标题与内容 → 给出下一篇动作 → 保存 Excel

## 两种模式

- **免费模式**：发送公众号后台截图、Excel/CSV或手动数字，不需要 API。
- **链接增强模式**：用户配置自己的世界树 API Key 后，通过文章链接读取互动数据。

安装后直接说：

```text
复盘这篇公众号文章的数据：截图、表格或文章链接
```

正常情况下，第一行会显示：

```text
已启用「公众号数据复盘 Skill」
```

## 它会交付什么

- 阅读量、点赞、分享、爱心/在看、总互动数和互动率。
- 标题结构、内容类型、选题类型和 CTA 的复盘。
- 表现亮点、可能原因、下一篇优化动作和待验证假设。
- 可持续追加的本地 Excel 复盘库。

只有一篇数据时，Skill 不会武断判断“好或差”；有 3 篇以上同账号、相近统计阶段的数据后，才使用历史中位数做内部比较。

## 下载与安装

[下载完整通用 Skill 包 v1.0.0](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/wechat-performance-v1.0.0/wechat-performance-review-skill-v1.0.0.zip)

### Codex

在 Codex 中发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-performance-review
```

### Claude Code

下载并解压通用 ZIP，把完整的 `wechat-performance-review` 文件夹放到：

```text
# 个人全局安装
~/.claude/skills/wechat-performance-review/

# 当前项目安装
.claude/skills/wechat-performance-review/
```

### WorkBuddy

1. 下载通用 ZIP。
2. 打开“技能”页面，选择“添加技能”→“上传技能”。
3. 上传 ZIP 并启用“公众号数据复盘”。
4. 新建任务，发送截图、表格或文章链接测试。

### OpenClaw（小龙虾）

下面整段命令要在运行 OpenClaw Gateway 的电脑或服务器系统终端中执行，不要发给聊天框：

```bash
cd "$HOME"
if [ -d "$HOME/yuanjiemi-ai-skills/.git" ]; then
  git -C "$HOME/yuanjiemi-ai-skills" pull
else
  git clone https://github.com/yuanjiemi/yuanjiemi-ai-skills.git "$HOME/yuanjiemi-ai-skills"
fi
openclaw skills install "$HOME/yuanjiemi-ai-skills/skills/wechat-performance-review" --as wechat-performance-review --global --force
```

安装后确认 `~/.openclaw/skills/wechat-performance-review/SKILL.md` 存在，重启 Gateway 并新开会话。配置和 Excel 都生成在运行 Gateway 的电脑或服务器上。

### 其他智能体

只要支持 Agent Skills / `SKILL.md`，就可以把完整文件夹安装到它规定的 Skills 目录。普通网页聊天机器人如果不支持 Skills，只能把 `SKILL.md` 作为项目指令，不能真正安装。

## 世界树增强模式

公开 Skill 不包含元子的 Key。用户第一次通过文章链接自动采集时，会看到申请和本机配置指引；已经配置“公众号对标文章采集与分析 Skill”的用户，可以自动复用原来的私有 Key。

不想申请 Key 时，发送后台截图、Excel/CSV或手动数字，仍可使用完整的免费复盘流程。

## 当前边界

- 不需要飞书 App ID 或 n8n。
- 不定时抓取，不登录公众号后台。
- 没有转化数据时，不把互动率说成商业转化率。
- 世界树增强模式使用用户自己的 Key，公开 Skill 不包含元子的 Key。

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
