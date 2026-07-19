# 公众号对标文章采集与分析 Skill

[← 返回全部 Skills](../../README.md)

把公众号对标内容变成可检索、可追溯、可继续写作的研究记录。

> 指定文章或账号 → 读取内容 → 按 21 个字段拆解 → 链接去重 → 保存本地 Excel → 生成适合自己 IP 的选题

## 两种使用模式

### 单篇免费模式

用户发送文章链接、正文、完整截图或可访问文档，即可完成拆解，不需要 API Key。

```text
拆解这篇公众号文章并收进对标研究库：文章链接或正文
```

微信文章链接无法被智能体读取时，补充正文或完整截图即可继续。

### 账号采集模式

用户配置自己的世界树 API Key 后，可以采集指定公众号最新 3 篇文章。新账号第一次需要提供该账号任意一篇文章链接，后续可以直接使用账号名称。

```text
采集“公众号名称”最新3篇文章并收进对标研究库
```

正常情况下，第一行会显示：

```text
已启用「公众号对标文章采集与分析 Skill」
```

## 交付内容

- 公众号对标账号研究库：21 个固定字段。
- 公众号对标源库：记录账号入口和最近采集情况。
- 带筛选、冻结窗格和字段说明的本地 Excel。
- 80–150 字研究结论。
- 3–5 个适合用户自己受众和 IP 的选题。
- 一个推荐优先选题及理由。

[下载空白 Excel 研究库模板](assets/公众号对标灵感库模板.xlsx)

## 下载与安装

[下载完整通用 Skill 包 v1.0.0](https://github.com/yuanjiemi/yuanjiemi-ai-skills/releases/download/wechat-benchmark-v1.0.0/wechat-benchmark-research-skill-v1.0.0.zip)

在 Codex 中发送：

```text
请用 $skill-installer 安装这个 Skill：
https://github.com/yuanjiemi/yuanjiemi-ai-skills/tree/main/skills/wechat-benchmark-research
```

其他支持 `SKILL.md` 的智能体，可以下载通用 ZIP，并把完整的 `wechat-benchmark-research` 文件夹安装到其 Skills 目录。不能只复制 `SKILL.md`，否则配置脚本和 Excel 模板会缺失。

## 账号采集：申请自己的世界树 API Key

公开 Skill 不包含、也不会共用元子的 Key。只有“按账号采集最新 3 篇”需要第三方 API；单篇文章拆解不需要 Key。

1. 打开[世界树官网](https://www.worldtreetech.cn/)，联系服务方申请自己的 API Key，并确认当前额度和计费规则。
2. 第一次运行账号采集时，Skill 会自动创建本机私有配置，并显示具体文件位置。
3. 只在自己电脑的配置文件中填写 Key，然后回复“已经配置好”。
4. 不要把 Key 发进聊天框、截图、Excel 或 GitHub。
5. 暂时不想申请，可以继续使用单篇免费模式。

[查看世界树接口文档](https://s.apifox.cn/2592d2ef-25b9-4e40-b92b-c1484ee35b14)

## 安全与功能边界

- 不要求飞书 App ID、App Secret、Cookie 或机器人配置。
- API Key 默认保存在用户自己的系统私有配置目录，不写入 GitHub、Excel 或采集结果。
- 默认只在用户发起任务时采集最新 3 篇，不做定时任务或完整历史抓取。
- 不登录微信公众号后台，不自动发布文章。
- 不自动写入飞书或 Notion；生成的 Excel 可以手动导入。
- 世界树是第三方服务，额度、价格和接口可用性由服务方决定。
