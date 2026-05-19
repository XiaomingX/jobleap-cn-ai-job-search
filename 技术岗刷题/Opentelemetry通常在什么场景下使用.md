# opentelemetry 通常在什么场景下使用，我可以本级部署以便理解和验证吗

**OpenTelemetry（简称 OTel）** 是目前云原生领域可观测性（Observability） 的事实标准。简单来说，它是为了解决分布式系统（微服务）中“查错难、监控难、分析难”的问题而生的。

下面为你拆解它的核心使用场景，并一步步教你在本地部署一套完整的验证环境。

---

## 一、 OpenTelemetry 通常在什么场景下使用？

在传统的单体应用中，看日志（Logs）和服务器指标（Metrics）就能解决大部分问题。但在现代架构中，OTel 主要解决以下四大痛点场景：

### 1. 分布式链路追踪（Distributed Tracing）

* **场景：** 用户反映“下单失败”或“接口响应慢”。在微服务架构中，一个请求可能经过了网关、Auth服务、订单服务、库存服务，最后读写了数据库。
* **OTel 的作用：** 它给每个请求生成一个唯一的 `Trace ID`。无论请求跨越多少个服务、数据库或消息队列，OTel 都能把整个调用链路串联起来，让你一眼看出**到底是哪个微服务卡了 2 秒，或者在哪个环节报错了**。

### 2. 统一可观测性数据（Metrics, Logs, Traces 三合一）

* **场景：** 以前看指标用 Prometheus，看日志用 ELK，看追踪用 Jaeger，三个系统互不相通，排查问题要在不同的 Tab 页之间切来切去。
* **OTel 的作用：** 它将 **Traces（链路）**、**Metrics（指标，如 CPU/内存/请求数）** 和 **Logs（日志）** 统一绑定。比如你可以直接从一个报错的 Trace 顺藤摸瓜，看到当时那个服务节点的 CPU 飙高指标，以及对应的详细错误日志。

### 3. 避免供应商锁定（Vendor Lock-in）

* **场景：** 公司原本使用 Datadog 或 Dynatrace 等商业监控软件，由于预算问题想换成开源的 Grafana + Prometheus 方案。如果以前用的是闭源 SDK，重构代码的成本高到崩溃。
* **OTel 的作用：** OTel 只负责**数据采集和标准化**。它不负责数据存储和展示。你可以随时通过改一下配置文件，把数据从 Datadog 切换投递到 Jaeger，**业务代码不需要改动哪怕一行**。

---

## 二、 我可以在本地部署以便理解和验证吗？

**完全可以，而且非常推荐！**

要在本地完美验证 OTel 的威力，你不需要自己从零写代码。OpenTelemetry 官方提供了一个极其优秀的示例项目：**OpenTelemetry Astronomy Shop（天文学商店）**。

这是一个包含了由 Go、Java、Python、Node.js、C# 等多语言编写的微服务电商系统，并且**内置了完整的 OTel 收集和展示链路（Jaeger、Prometheus、Grafana）**。

### 本地快捷部署步骤

确保你的电脑上安装了 **Docker** 和 **Docker Compose**。

#### 1. 克隆官方 Demo 仓库

打开终端（Terminal）并运行：

```bash
git clone https://github.com/open-telemetry/opentelemetry-demo.git
cd opentelemetry-demo

```

#### 2. 一键启动整个微服务集群

使用 Docker Compose 启动（首次运行需要下载镜像，可能需要几分钟）：

```bash
docker compose up --no-build -d

```

#### 3. 验证与玩转本地环境

启动成功后，你可以通过浏览器访问以下本地地址，亲身体验 OTel 的强大功能：

* **前端 Web 电商界面：** `http://localhost:8080`
* *你可以随便点点商品、加入购物车、下单，这些操作都会产生实时的数据流。*


* **Jaeger UI (查看 Traces 链路)：** `http://localhost:16686`
* *选择一个服务（如 `checkoutservice`），点击 "Find Traces"。你能看到你刚才点击下单时，请求是如何在各个微服务之间流转的。*


* **Grafana (查看 Metrics 和仪表盘)：** `http://localhost:3000`
* *默认进入后，可以看到预设的 OTel 仪表盘。这里展示了系统的吞吐量、错误率、响应时间等硬核指标。*



---

## 三、 本地验证时你应该重点观察什么？

为了加深理解，在本地环境跑起来后，你可以重点看这三个地方：

1. **OTel Collector（收集器）的存在：**
在架构中，所有的微服务并没有直接把数据发给 Jaeger 或 Grafana，而是统一发给了一个叫 `otel-collector` 的组件。这个组件负责接收、处理、批量转发数据。它是 OTel 的灵魂。
2. **代码的无侵入/低侵入性：**
你可以翻阅克隆下来的源码（比如 `src/shippingservice`）。你会发现，虽然它能输出那么详细的监控数据，但业务代码里几乎没有多少监控相关的逻辑，很多语言（如 Java、Node.js）甚至是通过自动插桩（Auto-instrumentation/Agent）直接实现监控的。

当然可以！在本地开发环境中部署 Jaeger 和 Prometheus 非常方便。

既然你已经在使用 `uv` 这种极速、现代的工具，那么在本地部署监控后端时，最推荐、最干净的方式就是使用 **Docker / Docker Compose**。这样不仅不会污染你的操作系统，还能完美模拟生产环境中的多组件协作。

下面为你提供一套在本地一键拉起 Jaeger、Prometheus 以及 OpenTelemetry Collector 的完整配置和使用指南。

---

## 一、 本地部署核心：Docker Compose 配置

在你的 FastAPI 项目根目录下，创建一个名为 `docker-compose.yml` 的文件。我们将通过它在本地一次性运行所有后端组件：

```yaml
version: '3.8'

services:
  # 1. OpenTelemetry Collector (收集器：负责接收 FastAPI 数据并分发)
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    volumes:
      - ./otel-config.yaml:/etc/otelcol/config.yaml
    ports:
      - "4317:4317" # gRPC 接收端口
      - "4318:4318" # HTTP 接收端口
    depends_on:
      - jaeger
      - prometheus

  # 2. Jaeger (链路追踪后端 + UI)
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686" # Jaeger UI 界面端口
      - "4317"        # 内部 gRPC 端口

  # 3. Prometheus (指标监控后端)
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yaml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090" # Prometheus UI 界面端口

```

---

## 二、 必要的配套配置文件

为了让这三个组件各司其职，我们需要为 Collector 和 Prometheus 提供简单的配置文件（同样放在项目根目录下）。

### 1. Collector 配置文件：`otel-config.yaml`

这个文件告诉 Collector：从 FastAPI 接收数据，然后分别发给 Jaeger 和 Prometheus。

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:

exporters:
  otlp/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true
  prometheus:
    endpoint: "0.0.0.0:8889"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/jaeger]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]

```

### 2. Prometheus 配置文件：`prometheus.yaml`

告诉 Prometheus 定期去 Collector 那里把指标数据“拉（Pull）”过来。

```yaml
global:
  scrape_interval: 5s # 为了本地测试灵敏，设为 5 秒抓取一次

scrape_configs:
  - job_name: 'otel-collector'
    static_configs:
      - targets: ['otel-collector:8889']

```

---

## 三、 本地运行与验证步骤

### 1. 启动后端组件

在终端执行以下命令，后台启动 Jaeger、Prometheus 和 Collector：

```bash
docker compose up -d

```

### 2. 使用 `uv` 启动你的 FastAPI 应用

保持上一节的配置，将数据发送到本地的 Collector（`localhost:4317`）：

```bash
export OTEL_SERVICE_NAME="fastapi-app"
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="otlp"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"

uv run opentelemetry-instrument uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```

### 3. 触发数据与查看结果

打开浏览器，访问 `http://localhost:8000/` 或 `http://localhost:8000/backend` 随便刷新几次，生成一些测试请求。

* **查看 Trace（链路追踪）**：
访问 **`http://localhost:16686`** 进入 Jaeger UI。在左侧 "Service" 下拉框选择 `fastapi-app`，点击 "Find Traces"，你就能看到每个 HTTP 请求的详细耗时、路由以及它请求外部 API 的下级 Span 瀑布图。
* **查看 Metrics（指标监控）**：
访问 **`http://localhost:9090`** 进入 Prometheus UI。在输入框中输入 `http_server_duration_milliseconds_count`（或者输入 `http` 会自动联想），点击 "Execute"，再切换到 "Graph" 标签页，就能看到请求量或延迟的折线图。

---

## 四、 总结

通过 `uv` 驱动的应用进程 + `Docker Compose` 运行的后端，你在本地就拥有了一套**企业级、标准化的现代可观测性演练场**。所有的组件（API -> SDK -> Collector -> Jaeger/Prometheus）都通过 OTLP 这一套标准协议无缝串联在了一起。

