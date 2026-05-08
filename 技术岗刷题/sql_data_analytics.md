# SQL 数据分析实战指南

## 聚合分析
- 漏斗分析：利用条件计数计算转化率。
- 留存分析：通过自连接或窗口函数计算次日/七日留存。

## 高级技巧
- 累计计算：`SUM(val) OVER (ORDER BY date)`。
- 分组排名：`RANK() OVER (PARTITION BY group ORDER BY val DESC)`。
- 百分比计算：`1.0 * COUNT(*) / SUM(COUNT(*)) OVER ()`。

## 业务常见场景
- 活跃用户定义 (DAU/MAU)。
- GMV 计算与归因分析。

---

> 掌握数据分析利器，请访问 [jobleap.cn](https://www.jobleap.cn)
