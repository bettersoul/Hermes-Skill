# 字段类型与值格式速查

| type | UI 类型 | 写入要求 | 示例 |
|------|---------|-----------|------|
| `1` | Text | 字符串 | `"Hermes 测试"` |
| `3` | SingleSelect | 选项中文名（非 ID） | `"选到了"` |
| `5` | DateTime | 毫秒时间戳（int） | `1782374400000` |
| `6` | MultiSelect | 字符串数组 | `["选项A", "选项B"]` |
| `7` | User | 用户 ID 数组 | `["ou_xxx", "ou_yyy"]` |

## 🕒 时间戳生成（Python）
```python
import time
# 2026-06-25 00:00:00 UTC
timestamp_ms = int(time.mktime(time.strptime("2026-06-25", "%Y-%m-%d")) * 1000)
print(timestamp_ms)  # → 1782374400000
```