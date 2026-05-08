# 基础设施与架构深度进阶 (MySQL, Redis, MQ, Zookeeper, Nginx)

## 一、数据库深度优化 (MySQL/MongoDB)
- **MySQL 锁机制**：表锁、行锁、间隙锁 (Gap Lock) 的应用场景。
- **事务 MVCC**：Undo Log 与 Read View 如何实现可重复读。
- **NoSQL 选型**：MongoDB 的副本集与分片集群原理。

## 二、分布式缓存 (Redis)
- **线程模型**：Redis 6.0 之后的多线程 I/O 与单线程执行核心。
- **集群架构**：Codis vs Redis Cluster 的优劣对比。
- **缓存应用**：如何利用 Redis 实现分布式限流、布隆过滤器。

## 三、消息队列与一致性 (MQ/ZK)
- **MQ 可靠性**：如何防止消息重复消费 (幂等性) 与消息丢失。
- **Zookeeper**：ZAB 协议原理、Watcher 机制的应用。

## 四、网络负载与安全 (Nginx)
- **反向代理**：七层 vs 四层负载均衡。
- **安全防护**：防止 SQL 注入、XSS 攻击、CSRF 攻击的 Nginx 配置策略。

---

> 提升技术深度，获取最新架构图谱，访问 [jobleap.cn](https://www.jobleap.cn)
