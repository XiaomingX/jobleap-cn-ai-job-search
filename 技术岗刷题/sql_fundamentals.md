# SQL 数据库面试精要

## 核心查询基础

### 1. 基础语法顺序
- 书写顺序：SELECT -> FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT
- 执行顺序：FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

### 2. 连接查询 (Joins)
- INNER JOIN：返回两表匹配的行。
- LEFT JOIN：返回左表所有行及匹配的右表行。
- FULL JOIN：返回两表所有的行。

### 3. 聚合与过滤
- GROUP BY：结合聚合函数 (COUNT, SUM, AVG, MAX, MIN) 使用。
- HAVING：对聚合后的结果进行过滤（WHERE 是对原始行过滤）。

---

## 进阶技术点

### 4. 窗口函数 (Window Functions)
在不减少行数的前提下进行聚合计算。
- 排序：RANK(), DENSE_RANK(), ROW_NUMBER()。
- 偏移：LAG(), LEAD()。
- 语法：`函数() OVER (PARTITION BY ... ORDER BY ...)`

### 5. 子查询与 CTE
- 子查询：嵌套在其他查询中的查询。
- CTE (WITH 语句)：使复杂查询结构更清晰，支持递归。

---

## 数据库底层与性能

### 6. 索引优化
- 聚簇索引与非聚簇索引。
- 覆盖索引：查询的所有列都在索引中，避免回表。
- 索引失效场景：使用函数、类型不匹配、模糊匹配开头用 % 等。

### 7. 事务 (Transaction)
- ACID 特性：原子性 (A)、一致性 (C)、隔离性 (I)、持久性 (D)。
- 隔离级别：读未提交、读已提交、可重复读 (MySQL 默认)、可串行化。

### 8. 慢查询排查
利用 `EXPLAIN` 分析执行计划，关注 type（是否全表扫描）、key（是否命中索引）和 rows。

---

> 提升 SQL 实战能力，请访问 [jobleap.cn](https://www.jobleap.cn)
