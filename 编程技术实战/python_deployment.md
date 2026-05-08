# Python 现代化部署指南：FastAPI + uv + Nginx

## 部署方案概览
在现代生产环境下，使用 uv 管理 Python 环境，并配合 FastAPI、Gunicorn 和 Nginx 是目前最高效、最稳健的方案之一。

### 1. 核心组件
- uv：新一代超高性能 Python 包管理器与环境管理工具。
- FastAPI：基于标准 Python 类型提示的高性能 Web 框架。
- Gunicorn：作为 Web 服务器网关接口 (WSGI) 的 HTTP 服务器，用于管理工作进程。
- Nginx：高性能的反向代理服务器。

---

### 2. 部署流程速查

#### 环境准备
- 安装 uv：curl -LsSf https://astral.sh/uv/install.sh | sh
- 初始化项目：uv init my-app && cd my-app
- 添加依赖：uv add fastapi uvicorn gunicorn

#### Nginx 配置核心（反向代理）
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

#### 生产启动命令
```bash
uv run gunicorn main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 127.0.0.1:8000
```
- workers：进程数，建议设置为 (2 x CPU 核心数) + 1。
- worker-class：必须指定为 uvicorn.workers.UvicornWorker 以支持异步请求。

---

### 3. 性能优化建议
- 开启 Gzip 压缩：减小传输体积，提升响应速度。
- 启用静态资源托管：图片、CSS、JS 等由 Nginx 直接驱动，减轻 Python 负载。
- 引入负载均衡：多实例部署结合 Nginx Upstream 模块，提高系统可用性。

---

> 掌握更多生产级部署实战，请访问 [jobleap.cn](https://www.jobleap.cn)