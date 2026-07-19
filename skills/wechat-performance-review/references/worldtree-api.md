# 世界树互动数据接入

## 接口

- `POST /api/v2/wechat/article/getInteraction`：通过文章 `link` 获取阅读、点赞、分享、爱心/在看等互动数据。
- `POST /api/v2/wechat/article/getDetail`：补充标题、作者、发布时间和正文，用于连接内容结构与数据。

请求只使用用户自己的 API Key。服务方字段可能调整，解析时兼容蛇形和驼峰命名；无法确认含义的字段不写入。

## 配置优先级

1. `WORLD_TREE_API_KEY` 或 `WORLDTREE_API_KEY` 环境变量。
2. 本 Skill 私有配置：`~/.config/yuanjiemi-ai-skills/wechat-performance-review/config.json`。
3. 已安装“公众号对标文章采集与分析 Skill”时，复用其私有配置：`~/.config/yuanjiemi-ai-skills/wechat-benchmark-research/config.json`。

Windows 使用 `%APPDATA%\yuanjiemi-ai-skills\...`。如果运行 OpenClaw Gateway，配置文件必须位于运行 Gateway 的电脑或服务器上。

## 安全

- 不要求用户把 Key 发到聊天框。
- 不把 Key 写入命令参数、日志、Excel、采集结果或 GitHub。
- API 报错内容必须先移除 Key 再显示。
- 公开模板中的 `api_key` 必须为空。

世界树是第三方服务，申请方式、价格、额度和接口可用性由服务方决定。用户不配置时切换截图、表格或手动数据模式。
