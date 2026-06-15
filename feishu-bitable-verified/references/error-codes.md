# 飞书 Bitable API 常见错误码

| code | 含义 | 原因 | 解决方案 |
|------|------|------|-----------|
| `99991663` | Invalid access token | token 过期、格式错误、权限不足 | ✅ 每次调用前重新 `POST /app_access_token/internal/` |
| `1254045` | FieldNameNotFound | 字段名不存在（拼写错/大小写错/空格错） | ✅ 先 `GET /fields` 获取真实 `field_name` |
| `99991672` | Access denied | 应用未开通 `bitable:app:write` 权限 | ✅ 在飞书开放平台 → 应用 → 权限管理 → 开通 |
| `1254047` | DatetimeFieldConvFail | 日期字段传了字符串（如 `"2026-06-25"`） | ✅ 传毫秒时间戳（如 `1782374400000`） |
| `99991662` | App not installed to base | 应用未安装到该 Base | ✅ 打开表格 → 右上角 ⋯ → 「添加应用」→ 选择你的应用 |
| `1254046` | RecordIdNotFound | 更新/删除时 record_id 错误 | ✅ 确保 `record_id` 来自 `POST /records` 的响应 |

> 📌 所有错误码均来自飞书官方文档：https://open.feishu.cn/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting