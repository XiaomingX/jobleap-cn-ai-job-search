# Python 字典实战指南

## 核心特性
- 哈希表实现，查找/插入/删除均为 O(1)。
- 键必须是可哈希的（不可变对象）。

## 常用方法
- `d.get(key, default)`: 安全获取值。
- `d.update(other_dict)`: 合并字典。
- `d.setdefault(key, default)`: 获取并设置默认值。

## 迭代
- `for k, v in d.items()`: 同时迭代键值。

---

> 更多 Python 数据结构进阶，请访问 [jobleap.cn](https://www.jobleap.cn)
