# Torn API

Torn API 提供遊戲資料查詢。端點、參數和權限以官方文件為準。

## 官方文件

| 文件 | 用途 |
|---|---|
| [Swagger UI](https://www.torn.com/swagger.php) | 查詢及試用 v2 端點 |
| [OpenAPI spec](https://www.torn.com/swagger/openapi.json) | 查詢 v2 參數與回應格式 |
| [API 說明](https://www.torn.com/api.html) | 查詢 v1 selections、Access Level、額度、cache 與使用條款 |

## 版本與認證

- v2 的 base URL 是 `https://api.torn.com/v2`。v1 的 selections 仍可使用；先查官方文件確認資料所屬版本。
- v2 可用 `Authorization: ApiKey <API_KEY>` header 傳入 API Key。v1 使用 `key` query 參數。
- API Key 有 Public、Minimal Access、Limited Access、Full Access 四種等級。每個 selection 的權限以官方文件為準。
- [API 說明](https://www.torn.com/api.html)以 `*` 標示 v1 專用 selection、`**` 標示 v2 專用 selection、`***` 標示兩版權限不同。
- API Key 不可寫入 wiki、commit 或公開紀錄。分享工具時只要求實際需要的權限，並遵守官方使用條款。

## 額度與 cache

- 官方文件目前列出每位玩家每分鐘 100 次 request，所有 Key 共用額度；限制可以變更。
- `timestamp` 讓 request 不同，可繞過 service cache；global cache 無法繞過。
- 批次查詢前，先查官方文件中的額度、cache 和端點參數。

## Sources

- [Torn API 說明](https://www.torn.com/api.html)
- [Torn Swagger UI](https://www.torn.com/swagger.php)
- [Torn OpenAPI spec](https://www.torn.com/swagger/openapi.json)
