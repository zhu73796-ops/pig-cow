---
name: pnw-pricing
description: Develop evidence-based sales-price proposals for Pink & White products or bundles. Use for 建议售价、价格带、套组定价、毛利测算、保本价 and 促销底价. Selling-point development belongs to pnw-selling-points.
---

# 粉与白产品价格

依据成本、渠道条件与产品价值证据，形成可审阅的价格方案。独立处理定价，不强制另做卖点提炼；需要开发购买理由时使用 `pnw-selling-points`。

## 当前电脑路径

开始时读取 [references/local-configuration.md](references/local-configuration.md)，解析本机配置中的路径。`{business_root}`、`{assets_root}`、`{skills_root}` 是配置占位符，不会自动展开。

## 产品身份与证据来源

已有商品通过 `product_id`、SPU、SKU 或链接码定位，不能仅凭名称关联。当前产品数据库路径：

`{business_root}/01_系统设计/企业管理/产品数据中心/database/product_master_v2.db`

数据库用于核对身份；Obsidian 产品事实源、已批准 Brief、BOM、样品评审及实物资料用于核对产品事实。先检查数据库是否可访问；外置盘未挂载时说明缺口，不新建同名空库。

`T260701A` 一类编码是产品专员开发项目组件码，不是产品编号或 SPU。可据此定位项目证据并讨论项目级候选；写入具体商品前需核实组件与产品的明确映射，不自行编造关联。

## 销售色名识别

按已核实产品/SKU读取原主档的“基础颜色—统一销售色名”关联及实际平台规格；用SKU承接成本和价格，不凭“乌鸦黑”等名称自动关联产品。淘宝、抖音、小红书共用已确认销售色名，定价方案沿用，价格技能不另起名、不改变基础颜色/编码、不因改名生成新库存身份。名称冲突仅限制受影响SKU的确定报价；其他清楚的SKU继续。规则见 `pnw-selling-points/references/sales-color-naming.md`。

## 定价方法与边界

先读 [references/aj-pricing-rules.md](references/aj-pricing-rules.md)，按 Obsidian 成本归纳与数据库读取生效 AJ 综合成本及版本，执行已确认的 2.4 系数、S/A 红线和折扣口径。不得重复追加 AJ 已含费用。再按 [references/decision-framework.md](references/decision-framework.md) 检查其他输入与套组关系；其费用拆分公式只适用于已拆出对应费用的成本，不能直接套在综合 AJ 上。

- 分清已确认事实、候选判断、待验证假设和已批准决策。
- 当前定价以毛利红线和可比竞品价格为核心，AJ×2.4 为参考起点，7/8/9 尾数仅做最后整理；不再把消费心理分流或尾数实验作为必需流程。
- 采购成本、BOM 材料成本、到手成本、产品毛利和贡献毛利分开；缺失成本不等于零。
- 不编造成本、供应商事实、市场价格、平台费率、目标毛利或活动规则。假设测算需明确列出假设，不能作为已知事实。
- 卖点或使用效果尚未证实时，不把它作为已验证的溢价依据。
- 建议售价在负责人批准前始终是提案；不写成已批准数据库值，不擅自修改线上售价。

## 最小有用输出

1. 产品身份、渠道、币种与成本版本；
2. 价格输入完整性及影响结论的缺口；
3. 输入支持时给出保本边界、建议常规价与活动底价，并附对应毛利或贡献口径；
4. 相关 SKU/套组结构、成本与真实优惠关系；
5. 冲突和下一步决策人，未知则待指定。

正式交接或准备数据库字段时读取 [references/output-contract.md](references/output-contract.md)。保持结果简洁，适合小团队评审。
