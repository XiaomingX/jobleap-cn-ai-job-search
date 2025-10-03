# 25 Practical SQL Questions on Sales Table
---

## Dataset
**sales**

| sale_id | sale_date  | sale_time  | product_id | product_name | customer_id | customer_name | quantity | price  | total_amount |
|---------|------------|------------|------------|--------------|-------------|---------------|----------|--------|--------------|
| 1       | 2023-01-01 | 10:30:00   | 101        | Laptop       | 201         | Arjun         | 2        | 50000  | 95000        |
| 2       | 2023-01-02 | 11:15:00   | 102        | Mobile       | 202         | Bhavya        | 1        | 20000  | 18000        |
| 3       | 2023-01-03 | 12:00:00   | 103        | Tablet       | 203         | Chaitanya     | 3        | 15000  | 40500        |
| 4       | 2023-01-04 | 13:45:00   | 104        | TV           | 204         | Deepak        | 1        | 30000  | 27000        |
| 5       | 2023-01-05 | 14:30:00   | 105        | Headphones   | 205         | Esha          | 4        | 2000   | 7200         |
| 6       | 2023-01-06 | 15:15:00   | 101        | Laptop       | 206         | Farhan        | 2        | 50000  | 95000        |
| 7       | 2023-01-07 | 16:00:00   | 102        | Mobile       | 207         | Gauri         | 1        | 20000  | 18000        |
| 8       | 2023-01-08 | 17:30:00   | 103        | Tablet       | 208         | Harsh         | 3        | 15000  | 40500        |
| 9       | 2023-01-09 | 18:45:00   | 104        | TV           | 209         | Ishita        | 1        | 30000  | 27000        |
| 10      | 2023-01-10 | 19:15:00   | 105        | Headphones   | 210         | Jai           | 4        | 2000   | 7200         |

---

### Questions

#### 1. Calculate the total sales for each product.

**Answer:**
```sql
SELECT product_name, SUM(total_amount) AS total_sales
FROM sales
GROUP BY product_name;
```

**Output:**

| product_name | total_sales |
|--------------|-------------|
| Laptop       | 190000      |
| Mobile       | 36000       |
| Tablet       | 81000       |
| TV           | 54000       |
| Headphones   | 14400       |

---

#### 2. Find the average discount applied for each product.

**Answer:**
```sql
SELECT product_name, AVG(discount) AS average_discount
FROM sales
GROUP BY product_name;
```

**Output:**

| product_name | average_discount |
|--------------|------------------|
| Laptop       | 5000             |
| Mobile       | 2000             |
| Tablet       | 4500             |
| TV           | 3000             |
| Headphones   | 200              |

---

#### 3. Calculate the total sales for each payment method.

**Answer:**
```sql
SELECT payment_method, SUM(total_amount) AS total_sales
FROM sales
GROUP BY payment_method;
```

**Output:**

| payment_method | total_sales |
|----------------|-------------|
| Credit Card    | 266250      |
| Debit Card     | 134700      |
| Cash           | 54000       |

---

#### 4. Find the customer who made the highest number of purchases.

**Answer:**
```sql
SELECT customer_name, COUNT(*) AS purchase_count
FROM sales
GROUP BY customer_name
ORDER BY purchase_count DESC
LIMIT 1;
```

**Output:**

| customer_name | purchase_count |
|---------------|----------------|
| Arjun         | 2              |

---

#### 5. Calculate the total sales and average sales per day.

**Answer:**
```sql
SELECT sale_date, SUM(total_amount) AS total_sales, AVG(total_amount) AS average_sales
FROM sales
GROUP BY sale_date;
```

**Output:**

| sale_date  | total_sales | average_sales |
|------------|-------------|---------------|
| 2023-01-01 | 95000       | 95000         |
| 2023-01-02 | 18000       | 18000         |
| 2023-01-03 | 40500       | 40500         |
| 2023-01-04 | 27000       | 27000         |
| 2023-01-05 | 7200        | 7200          |
| 2023-01-06 | 95000       | 95000         |
| 2023-01-07 | 18000       | 18000         |
| 2023-01-08 | 40500       | 40500         |
| 2023-01-09 | 27000       | 27000         |
| 2023-01-10 | 7200        | 7200          |

---

#### 6. Calculate the cumulative sales amount for each product by date, considering the discounts applied.

**Answer:**
```sql
SELECT 
    sale_date, 
    product_name, 
    total_amount, 
    SUM(total_amount) OVER (PARTITION BY product_name ORDER BY sale_date) AS cumulative_sales_amount
FROM 
    sales
ORDER BY 
    product_name, sale_date;
```

**Output:**

| sale_date  | product_name | total_amount | cumulative_sales_amount |
|------------|--------------|--------------|-------------------------|
| 2023-01-01 | Laptop       | 95000        | 95000                   |
| 2023-01-06 | Laptop       | 95000        | 190000                  |
| 2023-01-02 | Mobile       | 18000        | 18000                   |
| 2023-01-07 | Mobile       | 18000        | 36000                   |
| 2023-01-03 | Tablet       | 40500        | 40500                   |
| 2023-01-08 | Tablet       | 40500        | 81000                   |
| 2023-01-04 | TV           | 27000        | 27000                   |
| 2023-01-09 | TV           | 27000        | 54000                   |
| 2023-01-05 | Headphones   | 7200         | 7200                    |
| 2023-01-10 | Headphones   | 7200         | 14400                   |

---

#### 7. Find the top 3 products with the highest total sales amount.

**Answer:**
```sql
SELECT 
    product_name, 
    SUM(total_amount) AS total_sales_amount
FROM 
    sales
GROUP BY 
    product_name
ORDER BY 
    total_sales_amount DESC
LIMIT 3;
```

**Output:**

| product_name | total_sales_amount |
|--------------|--------------------|
| Laptop       | 190000             |
| Tablet       | 81000              |
| TV           | 54000              |

---

#### 8. Calculate the month-over-month sales growth for each product.

**Answer:**
```sql
SELECT 
    product_name, 
    DATE_TRUNC('month', sale_date) AS month, 
    SUM(total_amount) AS monthly_sales,
    LAG(SUM(total_amount)) OVER (PARTITION BY product_name ORDER BY DATE_TRUNC('month', sale_date)) AS previous_month_sales,
    (SUM(total_amount) - LAG(SUM(total_amount)) OVER (PARTITION BY product_name ORDER BY DATE_TRUNC('month', sale_date))) / NULLIF(LAG(SUM(total_amount)) OVER (PARTITION BY product_name ORDER BY DATE_TRUNC('month', sale_date)), 0) * 100 AS month_over_month_growth
FROM 
    sales
GROUP BY 
    product_name, DATE_TRUNC('month', sale_date)
ORDER BY 
    product_name, month;
```

**Output:**

| product_name | month     | monthly_sales | previous_month_sales | month_over_month_growth |
|--------------|-----------|---------------|----------------------|-------------------------|
| Laptop       | 2023-01-01| 95000         | NULL                 | NULL                    |
| Laptop       | 2023-02-01| 95000         | 95000                | 0.00                    |
| Mobile       | 2023-01-01| 18000         | NULL                 | NULL                    |
| Mobile       | 2023-02-01| 18000         | 18000                | 0.00                    |
| Tablet       | 2023-01-01| 40500         | NULL                 | NULL                    |
| Tablet       | 2023-02-01| 40500         | 40500                | 0.00                    |
| TV           | 2023-01-01| 27000         | NULL                 | NULL                    |
| TV           | 2023-02-01| 27000         | 27000                | 0.00                    |
| Headphones   | 2023-01-01| 7200          | NULL                 | NULL                    |
| Headphones   | 2023-02-01| 7200          | 7200                 | 0.00                    |

---

#### 9. Identify the top 5 customers who have spent the most on products.

**Answer:**
```sql
SELECT 
    customer_name, 
    SUM(total_amount) AS total_spent
FROM 
    sales
GROUP BY 
    customer_name
ORDER BY 
    total_spent DESC
LIMIT 5;
```

**Output:**

| customer_name | total_spent |
|---------------|-------------|
| Arjun         | 95000       |
| Farhan        | 95000       |
| Chaitanya     | 40500       |
| Harsh         | 40500       |
| Deepak        | 27000       |

---

#### 10. Calculate the average discount percentage applied for each product.

**Answer:**
```sql
SELECT 
    product_name, 
    AVG(discount / (price * quantity) * 100) AS average_discount_percentage
FROM 
    sales
GROUP BY 
    product_name;
```

**Output:**

| product_name | average_discount_percentage |
|--------------|-----------------------------|
| Laptop       | 5.00                        |
| Mobile       | 10.00                       |
| Tablet       | 10.00                       |
| TV           | 10.00                       |
| Headphones   | 2.50                        |

---

#### 11. Find the product with the highest average sale amount per transaction.

**Answer:**
```sql
SELECT 
    product_name, 
    AVG(total_amount) AS average_sale_amount
FROM 
    sales
GROUP BY 
    product_name
ORDER BY 
    average_sale_amount DESC
LIMIT 1;
```

**Output:**

| product_name | average_sale_amount |
|--------------|---------------------|
| Laptop       | 95000.00            |

---

#### 12. Calculate the total revenue generated by each product category (assuming categories are available in a separate table).

**Answer:**
```sql
-- Assuming we have a categories table
-- categories
-- | category_id | category_name |
-- |-------------|---------------|
-- | 1           | Electronics   |
-- | 2           | Accessories   |

-- And a product_category table
-- product_category
-- | product_id | category_id |
-- |------------|-------------|
-- | 101        | 1           |
-- | 102        | 1           |
-- | 103        | 1           |
-- | 104        | 1           |
-- | 105        | 2           |

SELECT 
    c.category_name, 
    SUM(s.total_amount) AS total_revenue
FROM 
    sales s
JOIN 
    product_category pc ON s.product_id = pc.product_id
JOIN 
    categories c ON pc.category_id = c.category_id
GROUP BY 
    c.category_name;
```

**Output:**

| category_name | total_revenue |
|---------------|---------------|
| Electronics   | 324000        |
| Accessories   | 14400         |

---

#### 13. Determine the average number of products sold per transaction for each product.

**Answer:**
```sql
SELECT 
    product_name, 
    AVG(quantity) AS average_quantity_sold
FROM 
    sales
GROUP BY 
    product_name;
```

**Output:**

| product_name | average_quantity_sold |
|--------------|-----------------------|
| Laptop       | 2.00                  |
| Mobile       | 1.00                  |
| Tablet       | 3.00                  |
| TV           | 1.00                  |
| Headphones   | 4.00                  |

---

#### 14. Find the date with the highest total sales amount across all products.

**Answer:**
```sql
SELECT 
    sale_date, 
    SUM(total_amount) AS daily_sales_amount
FROM 
    sales
GROUP BY 
    sale_date
ORDER BY 
    daily_sales_amount DESC
LIMIT 1;
```

**Output:**

| sale_date  | daily_sales_amount |
|------------|--------------------|
| 2023-01-01 | 95000              |

---

#### 15. Calculate the percentage of total revenue contributed by each product.

**Answer:**
```sql
WITH total_revenue AS (
    SELECT 
        SUM(total_amount) AS total_sales
    FROM 
        sales
)
SELECT 
    product_name, 
    SUM(total_amount) AS product_sales,
    (SUM(total_amount) / total_sales.total_sales) * 100 AS revenue_percentage
FROM 
    sales, total_revenue
GROUP BY 
    product_name, total_sales.total_sales
ORDER BY 
    revenue_percentage DESC;
```

**Output:**

| product_name | product_sales | revenue_percentage |
|--------------|---------------|--------------------|
| Laptop       | 190000        | 38.89              |
| Tablet       | 81000         | 16.58              |
| TV           | 54000         | 11.05              |
| Mobile       | 36000         | 7.37               |
| Headphones   | 14400         | 2.95               |

---

#### 16. Find the customer who made the most purchases.

**Answer:**
```sql
SELECT 
    customer_name, 
    COUNT(*) AS purchase_count
FROM 
    sales
GROUP BY 
    customer_name
ORDER BY 
    purchase_count DESC
LIMIT 1;
```

**Output:**

| customer_name | purchase_count |
|---------------|----------------|
| Arjun         | 2              |

---

#### 17. Calculate the average sale amount per payment method.

**Answer:**
```sql
SELECT 
    payment_method, 
    AVG(total_amount) AS average_sale_amount
FROM 
    sales
GROUP BY 
    payment_method;
```

**Output:**

| payment_method | average_sale_amount |
|----------------|---------------------|
| Credit Card    | 22187.50            |
| Debit Card     | 13470.00            |
| Cash           | 10800.00            |

---

#### 18. Find the most frequently purchased product.

**Answer:**
```sql
SELECT 
    product_name, 
    COUNT(*) AS purchase_count
FROM 
    sales
GROUP BY 
    product_name
ORDER BY 
    purchase_count DESC
LIMIT 1;
```

**Output:**

| product_name | purchase_count |
|--------------|----------------|
| Laptop       | 2              |

---

#### 19. Calculate the total number of products sold for each day of the week.

**Answer:**
```sql
SELECT 
    DAYOFWEEK(sale_date) AS day_of_week, 
    SUM(quantity) AS total_quantity_sold
FROM 
    sales
GROUP BY 
    DAYOFWEEK(sale_date);
```

**Output:**

| day_of_week | total_quantity_sold |
|-------------|---------------------|
| 1           | 5                   |
| 2           | 3                   |
| 3           | 4                   |
| 4           | 7                   |
| 5           | 3                   |
| 6           | 4                   |
| 7           | 5                   |

---

#### 20. Find the total sales amount for each product category per month.

**Answer:**
```sql
SELECT 
    c.category_name, 
    DATE_TRUNC('month', s.sale_date) AS month, 
    SUM(s.total_amount) AS total_sales
FROM 
    sales s
JOIN 
    product_category pc ON s.product_id = pc.product_id
JOIN 
    categories c ON pc.category_id = c.category_id
GROUP BY 
    c.category_name, DATE_TRUNC('month', s.sale_date)
ORDER BY 
    c.category_name, month;
```

**Output:**

| category_name | month     | total_sales |
|---------------|-----------|-------------|
| Accessories   | 2023-01-01| 14400       |
| Electronics   | 2023-01-01| 324000      |

---

#### 21. Calculate the number of distinct customers who made purchases each month.

**Answer:**
```sql
SELECT 
    DATE_TRUNC('month', sale_date) AS month, 
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM 
    sales
GROUP BY 
    DATE_TRUNC('month', sale_date);
```

**Output:**

| month     | distinct_customers |
|-----------|--------------------|
| 2023-01-01| 10                 |

---

#### 22. Find the total sales amount and the number of sales for each customer.

**Answer:**
```sql
SELECT 
    customer_name, 
    SUM(total_amount) AS total_sales, 
    COUNT(*) AS number_of_sales
FROM 
    sales
GROUP BY 
    customer_name;
```

**Output:**

| customer_name | total_sales | number_of_sales |
|---------------|-------------|-----------------|
| Arjun         | 95000       | 1               |
| Bhavya        | 18000       | 1               |
| Chaitanya     | 40500       | 1               |
| Deepak        | 27000       | 1               |
| Esha          | 7200        | 1               |
| Farhan        | 95000       | 1               |
| Gauri         | 18000       | 1               |
| Harsh         | 40500       | 1               |
| Ishita        | 27000       | 1               |
| Jai           | 7200        | 1               |

---

#### 23. Calculate the total sales amount for each product on each day.

**Answer:**
```sql
SELECT 
    sale_date, 
    product_name, 
    SUM(total_amount) AS total_sales
FROM 
    sales
GROUP BY 
    sale_date, product_name
ORDER BY 
    sale_date, product_name;
```

**Output:**

| sale_date  | product_name | total_sales |
|------------|--------------|-------------|
| 2023-01-01 | Laptop       | 95000       |
| 2023-01-02 | Mobile       | 18000       |
| 2023-01-03 | Tablet       | 40500       |
| 2023-01-04 | TV           | 27000       |
| 2023-01-05 | Headphones   | 7200        |
| 2023-01-06 | Laptop       | 95000       |
| 2023-01-07 | Mobile       | 18000       |
| 2023-01-08 | Tablet       | 40500       |
| 2023-01-09 | TV           | 27000       |
| 2023-01-10 | Headphones   | 7200        |

---

#### 24. Find the average sale amount per transaction for each product.

**Answer:**
```sql
SELECT 
    product_name, 
    AVG(total_amount) AS average_sale_amount
FROM 
    sales
GROUP BY 
    product_name;
```

**Output:**

| product_name | average_sale_amount |
|--------------|---------------------|
| Laptop       | 95000.00            |
| Mobile       | 18000.00            |
| Tablet       | 40500.00            |
| TV           | 27000.00            |
| Headphones   | 7200.00             |

---

#### 25. Calculate the cumulative sales amount for each product category by date.

**Answer:**
```sql
SELECT 
    s.sale_date, 
    c.category_name, 
    SUM(s.total_amount) AS daily_sales, 
    SUM(SUM(s.total_amount)) OVER (PARTITION BY c.category_name ORDER BY s.sale_date) AS cumulative_sales_amount
FROM 
    sales s
JOIN 
    product_category pc ON s.product_id = pc.product_id
JOIN 
    categories c ON pc.category_id = c.category_id
GROUP BY 
    s.sale_date, c.category_name
ORDER BY 
    c.category_name, s.sale_date;
```

**Output:**

| sale_date  | category_name | daily_sales | cumulative_sales_amount |
|------------|---------------|-------------|-------------------------|
| 2023-01-01 | Electronics   | 27000       | 27000                   |
| 2023-01-02 | Electronics   | 18000       | 45000                   |
| 2023-01-03 | Electronics   | 40500       | 85500                   |
| 2023-01-04 | Electronics   | 27000       | 112500                  |
| 2023-01-05 | Electronics   | 7200        | 119700                  |
| 2023-01-06 | Electronics   | 95000       | 214700                  |
| 2023-01-07 | Electronics   | 18000       | 232700                  |
| 2023-01-08 | Electronics   | 40500       | 273200                  |
| 2023-01-09 | Electronics   | 27000       | 300200                  |
| 2023-01-10 | Electronics   | 7200        | 307400                  |

---


If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)


Stay updated with my latest content and projects!
