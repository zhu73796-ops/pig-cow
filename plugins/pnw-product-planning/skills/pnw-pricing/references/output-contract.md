# 价格正式交接

## 会议版

- 产品 ID / SPU、渠道、币种、当前阶段与证据日期。
- 已知成本口径及缺失输入。
- 保本边界、建议常规价或区间、活动底价或不可计算原因。
- 对应毛利/贡献结果、套组分配与真实优惠额（如适用）。
- 只列会改变价格结论的关键问题，并标明决策人；未知则待指定。

## 确认后准备的字段

- `product_id`
- `price_type`：regular / launch / promotion_floor
- `price_amount`
- `currency`
- `channel`
- `effective_from`
- `cost_basis_date`
- `approval_status`
- `approved_by`
- `source_document`

以上是交接字段建议，不代表现有数据库已经具备相同字段。写入前检查实际结构及任务授权；保留价格版本和来源，不覆盖历史批准记录。
