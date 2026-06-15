---
name: feishu-bitable-verified
category: feishu
description: 飞书多维表格（Bitable）生产级读写技能 —— 严格遵循飞书官方 API 流程，支持自动 token 刷新、字段探测、主键校验、文本/单选/日期字段安全写入
author: Hermes Agent + 用户验证
version: 1.0.0
---

## 🌟 技能价值
> 这不是“又一个脚本”，而是你亲手验证的**生产级工作流封装**。

✅ 已验证场景：
- 表 `tblL6w2IpYbLZDHe`（字段：`所遇到的问题`/`解决方案`）
- 成功写入 4 条记录（含问题日志）
- 全部使用 `requests.post(..., json=data)`，零 `curl` shell 问题

## 🔁 核心流程（6 步闭环，不可跳过）
1. **获取 token**：`POST /auth/v3/app_access_token/internal/`（每次调用前）
2. **探测字段**：`GET /apps/{base_id}/tables/{table_id}/fields`
3. **校验主键**：检查 `is_primary: true` 字段是否存在且非空
4. **构造数据**：按 `field_name` 键名，填入对应类型值（文本=字符串，单选=选项名，日期=毫秒戳）
5. **发送请求**：`POST /records`，header 精确（`Authorization` + `Content-Type`）
6. **解析响应**：检查 `code: 0` + `record_id`，失败立即报错

## 🚨 常见错误码（飞书官方）
| code | 含义 | 解决方案 |
|------|------|-----------|
| `99991663` | token 无效（过期/格式错） | ✅ 每次调用前重新获取 |
| `1254045` | 字段名不存在 | ✅ 用 `GET /fields` 确认真实字段名 |
| `99991672` | 权限不足 | ✅ 在飞书开放平台开通 `bitable:app:write` |
| `1254047` | 日期格式错误 | ✅ 传毫秒时间戳，非字符串 |

## 📚 字段类型速查
| type | UI 类型 | 写入值示例 | Python 示例 |
|------|---------|-------------|--------------|
| `1` | Text | `"Hermes 测试"` | `"Hermes 测试"` |
| `3` | SingleSelect | `"选到了"` | `"选到了"` |
| `5` | DateTime | `1782374400000` | `int(time.mktime(time.strptime("2026-06-25", "%Y-%m-%d")) * 1000)` |

## 🛠️ 使用示例
```python
# 读取表格
read_table(base_id="ICVCcx6m5nbh", table_id="tw2IpYbLZDHe")

# 写入单条记录
write_record(
  base_id="ICVCcx6m5nbh", 
  table_id="tw2IpYbLZDHe",
  fields={"所遇到的问题": "Hermes 写入验证", "解决方案": "已验证流程"}
)

# 批量写入
write_batch(
  base_id="ICVCcx6m5nbh", 
  table_id="tw2IpYbLZDHe",
  records=[
    {"所遇到的问题": "测试 #1"},
    {"所遇到的问题": "测试 #2"}
  ]
)
```