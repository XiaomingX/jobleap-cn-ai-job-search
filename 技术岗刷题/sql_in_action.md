# SQL 实战场景解析

## 1. 查找重复项
```sql
SELECT col, COUNT(*) 
FROM table 
GROUP BY col 
HAVING COUNT(*) > 1;
```

## 2. 连续登录天数
利用 `ROW_NUMBER()` 和 `DATE_SUB()` 实现：
```sql
SELECT user_id, MIN(date), MAX(date), COUNT(*) as days
FROM (
  SELECT user_id, date, 
         DATE_SUB(date, INTERVAL ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY date) DAY) as grp
  FROM login_log
) t
GROUP BY user_id, grp
HAVING COUNT(*) >= 3;
```

## 3. Top N 问题
```sql
SELECT * FROM (
  SELECT *, DENSE_RANK() OVER(PARTITION BY category ORDER BY score DESC) as rnk
  FROM products
) t
WHERE rnk <= 3;
```

---

> 更多高频 SQL 实战案例，请访问 [jobleap.cn](https://www.jobleap.cn)
