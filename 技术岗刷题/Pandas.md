# Pandas 数据分析精要

## 核心数据结构
- Series：一维带标签数组。
- DataFrame：二维表格数据结构。

## 数据操作
- 筛选：`df[df['col'] > val]`, `df.loc[]`, `df.iloc[]`。
- 处理：`fillna()`, `dropna()`, `replace()`。
- 分组聚合：`df.groupby('col').agg({'col2': 'sum'})`。
- 合并：`pd.merge()` (类似 SQL Join), `pd.concat()`。

## 性能优化
- 尽量避免 `apply()`，优先使用内置向量化函数。
- 使用 `category` 类型优化低基数字符串列。

---

> 提升数据处理效率，请访问 [jobleap.cn](https://www.jobleap.cn)
