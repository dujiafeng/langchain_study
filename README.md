     1|     1|# LangChain Study
     2|     2|
     3|     3|LangChain / Deep Agents 学习笔记，基于官方文档整理为 Jupyter Notebook。
     4|     4|
     5|     5|---
     6|     6|
     7|     7|## 学习路径
     8|     8|
     9|     9|共 10 个阶段，建议按顺序学习。每阶段标注了前置依赖和核心产出。
    10|    10|
    11|    11|---
    12|    12|
    13|    13|### 第一阶段：入门基础
    14|    14|
    15|    15|**目标：** 理解 LangChain 的设计哲学、核心组件，跑通第一个 Agent。
    16|    16|
    17|    17|**前置知识：** Python 基础、LLM 基本概念（API Key、Temperature 等）。
    18|    18|
    19|    19|| 步骤 | Notebook | 核心知识点 | 产出 |
    20|    20||:----:|----------|-----------|------|
    21|    21|| 1 | `langchain/01_入门基础/01_概述与理念` | 组合优先、最小抽象、渐进式披露、Provider 无关、可观测性优先 — 五大设计理念；核心组件生态图(Mermaid)：输入处理 → 嵌入 → 检索 → 生成 → 编排；RAG 流、Agent 工具流、多 Agent 系统架构图 | 理解 LangChain 定位 |
    22|    22|| 2 | `langchain/01_入门基础/02_快速入门` | `pip install` 各 Provider 包、`create_agent` 最简用法、`init_chat_model` 统一模型接口、`invoke`/`stream` 调用方式、多 Provider 切换表（OpenAI/Anthropic/Google/DeepSeek/OpenRouter 等）、LangSmith 追踪设置 | 跑通第一个 Agent |
    23|    23|| 3 | `langchain/02_模型与工具/01_模型与消息` | `init_chat_model` 核心参数表(temperature/max_tokens/timeout/max_retries)、重试策略(指数退避、429/5xx 自动重试、401/404 不重试)、4 种消息类型(SystemMessage/HumanMessage/AIMessage/ToolMessage)、`invoke`/`stream`/`batch` 三种调用方法、带对话历史的完整示例 | 掌握模型配置与消息结构 |
    24|    24|| 4 | `langchain/02_模型与工具/02_工具与结构化输出` | `@tool` 装饰器 vs BaseTool 类 vs Tool dict 三种定义方式、`parse_docstring` 参数描述、`response_format` Pydantic schema 结构化输出、TypedDict 轻量选择 | 能自定义工具和输出格式 |
    25|    25|
    26|    26|---
    27|    27|
    28|    28|### 第二阶段：Agent 核心
    29|    29|
    30|    30|**目标：** 掌握 `create_agent` 的完整参数体系，理解上下文管理和中间件机制。
    31|    31|
    32|    32|**前置依赖：** 第一阶段完成。
    33|    33|
    34|    34|| 步骤 | Notebook | 核心知识点 | 产出 |
    35|    35||:----:|----------|-----------|------|
    36|    36|| 1 | `langchain/03_Agent与RAG/01_Agent详解` | `create_agent` 全部参数详解(model/tools/system_prompt/response_format/checkpointer/context_schema/middleware/state_schema/name/interrupt_on)、工具 4 种定义方式(函数/@tool/BaseTool/dict)、system_prompt 层级、Memory 文件(AGENTS.md)、结构化输出(Pydantic)、invoke/ainvoke/stream/stream_events v3 四种调用方式、5 种沙箱后端(Modal/Runloop/Daytona/LangSmith/AgentCore)代码示例、文件系统操作表(ls/read_file/write_file/edit_file/glob/grep/execute)、技能发现路径、子 Agent 配置字段 | 完整掌握 Agent 构建 |
    37|    37|| 2 | `langchain/04_记忆与上下文/01_上下文与记忆` | Agent 失效的 #1 原因（上下文缺失）、可控上下文 3 种类型(Model/Tool/Lifecycle)、3 种数据源(Runtime Context/State/Store)作用域对比、`@dynamic_prompt` 从 state/store/runtime 动态生成 system prompt、`@wrap_model_call` 拦截模型调用注入上下文、Checkpointer 持久化(InMemorySaver)、Store KV API(InMemoryStore + get/put)、短期记忆(thread_id 对话保持)、长期记忆(跨对话用户偏好) | 理解上下文工程的底层实现 |
    38|    38|| 3 | `langchain/06_中间件/01_中间件` | 10 种内置中间件(Summarization/TodoList/SubAgent/Rubric/Interpreter/Filesystem/Skills/CodeExecution/Permissions/ContextHub)、3 种中间件类型对比(@dynamic_prompt/@wrap_model_call/@lifecycle)、`request.override()` 可修改的属性(model/messages/tools/system_prompt)、自定义 Middleware 类编写(实现 `__call__` 接口)、实际示例：记录中间件、重试中间件、速率限制中间件 | 掌握 LangChain 核心扩展机制 |
    39|    39|| 4 | `langchain/05_运行时与流式/02_运行时与MCP` | Runtime 三组件(Context/State/Store)详解、ToolRuntime 接口访问 runtime.context/state/store、Checkpointer 生命周期(thread_id 全程追踪)、Store KV API 完整用法(namespace/key/value)、MCP 协议简介、4 种传输方式(stdio/HTTP/SSE/WebSocket)、3 级自动发现位置、工具过滤配置 | 理解运行时和外部工具集成 |
    40|    40|
    41|    41|---
    42|    42|
    43|    43|### 第三阶段：Deep Agents（开箱即用框架）
    44|    44|
    45|    45|**目标：** 掌握 LangChain 团队推荐的"电池包"式 Agent 框架，理解其与 `create_agent` 的关系。
    46|    46|
    47|    47|**前置依赖：** 第一、二阶段完成（了解 LangChain 核心概念即可）。
    48|    48|
    49|    49|| 步骤 | Notebook | 核心知识点 | 产出 |
    50|    50||:----:|----------|-----------|------|
    51|    51|| 1 | `deepagents/01_核心概念/01_概述` | Deep Agents vs LangChain vs LangGraph 定位对比、Harness 四大组件(执行环境/上下文管理/委派/引导)、一句话创建 Agent(create_deep_agent)、多 Provider 支持、框架关系 | 理解 Deep Agents 定位 |
    52|    52|| 2 | `deepagents/01_核心概念/02_快速入门` | 完整 5 步流程：安装→API Key→搜索工具→创建 Agent→运行、Tavily 搜索集成、`agent.invoke()` 与 `agent.stream()` 调用 | 搭建第一个 Deep Agent |
    53|    53|| 3 | `deepagents/01_核心概念/03_框架能力` | 执行环境四层(Tools/虚拟文件系统/权限/代码执行)、上下文管理四层(Skills/Memory/摘要与卸载/Prompt Caching)、委派(任务规划 write_todos + 子 Agent)、引导(HITL interrupt_on)、Harness Profile 注册、多模态文件支持(图片/视频/音频/文档)、文件系统工具全表 | 全面了解框架内置能力 |
    54|    54|| 4 | `deepagents/02_模型与配置/01_模型` | `provider:model` 格式规范、完整 Provider 列表与建议模型(Google/OpenAI/Anthropic/Open-weight)、`init_chat_model` 统一入口、关键参数表、3 种调用方法、字符串 vs Model 实例两种传参方式、`ProviderProfile` 统一配置管理(Provider 级 + 模型级继承)、Middleware 动态切换模型 | 掌握模型配置体系 |
    55|    55|| 5 | `deepagents/02_模型与配置/02_自定义` | 自定义 System Prompt、自定义 Tools(`@tool(parse_docstring=True)`)、自定义 Middleware、`HarnessProfile` 配置 Bundle、`excluded_tools` 排除工具 | 能按需定制 Deep Agent |
    56|    56|
    57|    57|---
    58|    58|
    59|    59|### 第四阶段：上下文与记忆
    60|    60|
    61|    61|**目标：** 深入理解 Agent 上下文管理的完整方案，从输入控制到跨对话持久化。
    62|    62|
    63|    63|**前置依赖：** 第二、三阶段完成。
    64|    64|
    65|    65|| 步骤 | Notebook | 核心知识点 | 产出 |
    66|    66||:----:|----------|-----------|------|
    67|    67|| 1 | `deepagents/03_上下文与记忆/01_上下文工程` | 5 种上下文类型一览表(Input/Runtime/Compression/Isolation/Long-term)、Input Context 四要素(System Prompt/Memory/Skills/Tool Prompts)、完整 System Prompt 组装顺序(9 步)、Runtime Context 定义与访问(context_schema + ToolRuntime)、Context Compression(Offloading + Summarization)、Subagent 上下文隔离、Long-term Memory 虚拟文件系统、最佳实践总结表 | 系统性理解上下文工程 |
    68|    68|| 2 | `deepagents/03_上下文与记忆/02_长期记忆` | 记忆工作方式(Agent 作用域/用户作用域/情景记忆/组织级记忆)、Store KV API(InMemoryStore + namespace/key/value)、后台合并模式(合并 Agent + Cron)、只读 vs 可写记忆、并发写入策略、多 Agent 隔离 | 实现跨对话持久化 |
    69|    69|| 3 | `deepagents/03_上下文与记忆/03_技能` | Skills 目录结构(SKILL.md + frontmatter)、渐进式披露原理(只读 frontmatter，需要时加载全文)、3 种 Backend 示例(StateBackend/StoreBackend/FilesystemBackend)、解释器技能中间件 | 构建可复用的技能模块 |
    70|    70|| 4 | `deepagents/03_上下文与记忆/04_权限` | `FilesystemPermission` 规则结构(operations/paths/mode)、规则排序陷阱(First-match-wins)、5 个场景(只读 Agent/工作区隔离/保护敏感文件/只读记忆/拒绝全部)、Subagent 独立权限继承、CompositeBackend 沙箱限制 | 掌握 Agent 文件系统安全 |
    71|    71|
    72|    72|---
    73|    73|
    74|    74|### 第五阶段：执行模式
    75|    75|
    76|    76|**目标：** 掌握 Agent 的各种执行模式 — 流式、事件流、子 Agent、审批。
    77|    77|
    78|    78|**前置依赖：** 第三阶段完成。
    79|    79|
    80|    80|| 步骤 | Notebook | 核心知识点 | 产出 |
    81|    81||:----:|----------|-----------|------|
    82|    82|| 1 | `deepagents/04_执行模式/01_流式输出` | `agent.stream()` 基础用法、`stream_mode` 参数(updates/values/custom)、subgraph streaming(namespace 路由)、生命周期追踪 | 实现基础流式输出 |
    83|    83|| 2 | `deepagents/04_执行模式/02_事件流` | `stream_events(version="v3")` vs `stream()` 对比、6 种投影(messages/values/tool_calls/subgraphs/output/extensions)、`message.text`/`message.reasoning`/`message.tool_calls` 增量访问、`stream.subgraphs` 嵌套流、`stream.tool_calls` 生命周期、v2 格式兼容、interleave 交错消费 | 掌握事件流全部投影 |
    84|    84|| 3 | `deepagents/04_执行模式/03_异步子Agent` | `AsyncSubAgent` 配置、生命周期管理(创建/进度/取消/完成)、部署选项(ASGI/HTTP/混合)、`task.async_task` 创建、`check_progress` 检查进度、`cancel_task` 取消、`stream_subagent` 实时流 | 实现后台异步任务 |
    85|    85|| 4 | `deepagents/04_执行模式/04_子Agent` | 字典 vs `CompiledSubAgent` 两种配置方式、结构化输出(SubAgent structured_output)、技能继承(subagent skills)、上下文传播(runtime context 自动传播)、`task` 工具调用、并行子 Agent | 掌握隔离执行 |
    86|    86|| 5 | `deepagents/04_执行模式/05_人类审批` | `interrupt_on` 配置、决策类型(approve/edit/reject/response)、多工具批处理审批、`resume_with` 继续执行、Subagent 中断、`@on_interrupt` 回调 | 实现安全审批流程 |
    87|    87|| 6 | `deepagents/04_执行模式/06_Agent到Agent` | A2A 协议概念、Agent 间通信模式 | 了解 Agent 互连 |
    88|    88|| 7 | `deepagents/04_执行模式/07_通信协议` | ACP 协议、ACP Server 配置、Zed/Toad IDE 集成 | 了解 Agent 协议 |
    89|    89|
    90|    90|---
    91|    91|
    92|    92|### 第六阶段：多 Agent 系统
    93|    93|
    94|    94|**目标：** 掌握构建多个 Agent 协作系统的 5 种模式。
    95|    95|
    96|    96|**前置依赖：** 第二、三阶段完成。
    97|    97|
    98|    98|| 步骤 | Notebook | 核心知识点 | 产出 |
    99|    99||:----:|----------|-----------|------|
   100|   100|| 1 | `langchain/07_多Agent/01_核心模式` | 4 种模式对比表(交接/子Agent/路由/技能)、Handoff 节点路由、SubAgent 创建(task 工具)、Router 条件边路由、SkillsMiddleware 渐进式披露、代码示例 | 掌握多 Agent 核心模式 |
   101|   101|| 2 | `langchain/07_多Agent/02_自定义工作流` | LangGraph `StateGraph` 构建、节点定义、条件边、人工边、状态管理(MessagesState)、编译执行、异步支持 | 能编排任意拓扑 |
   102|   102|| 3 | `langchain/07_多Agent/03_示例` | 4 个完整示例：客服交接(三 Agent)、知识库路由(路由器+知识库 Agent)、SQL 助手(技能)、个人助手(子 Agent 架构) | 参考实现多 Agent 系统 |
   103|   103|
   104|   104|---
   105|   105|
   106|   106|### 第七阶段：RAG 与检索
   107|   107|
   108|   108|**目标：** 为 Agent 注入外部知识，构建 RAG 应用。
   109|   109|
   110|   110|**前置依赖：** 第二、三阶段完成。
   111|   111|
   112|   112|| 步骤 | Notebook | 核心知识点 | 产出 |
   113|   113||:----:|----------|-----------|------|
   114|   114|| 1 | `langchain/03_Agent与RAG/02_RAG与检索` | RAG 三阶段流程(索引→检索→生成)、6 种文档加载器(Text/PDF/CSV/Web/YouTube/Slack)、5 种文本分割器对比(RecursiveCharacter/Semantic/Code/Markdown/Token)、10 种向量存储对比(Chroma/Pinecone/FAISS/Weaviate/Qdrant/Milvus/PGVecto.rs/Supabase/Elasticsearch/Redis)、6 种检索器类型(Vector/BM25/Hybrid/Contextual/MultiQuery/ParentDocument)、5 种高级 RAG 技术(Self-RAG/Corrective RAG/Adaptive RAG/Fusion/Speculative RAG)、完整 RAG 链代码 | 掌握 RAG 全栈 |
   115|   115|| 2 | `langchain/03_Agent与RAG/03_SQL与语音` | SQL Agent 架构(Database → Toolkit → LLM → SQL → Result)、SQLDatabaseToolkit 详解(7 种工具)、7 种数据库连接类型(SQLite/PostgreSQL/MySQL/MariaDB/MSSQL/Oracle/BigQuery)、语音栈三组件(STT/LLM/TTS)对比表、Voice Stack 5 项最佳实践 | 扩展 Agent 交互方式 |
   116|   116|| 3 | `deepagents/06_应用场景/01_深度研究` | Tavily 搜索工具、多子 Agent 编排、研究流程模板 | 研究型 Agent 实战 |
   117|   117|| 4 | `deepagents/06_应用场景/02_内容构建` | AGENTS.md 品牌记忆、技能系统、Gemini 图片生成 | 内容 Agent 实战 |
   118|   118|| 5 | `deepagents/06_应用场景/03_数据分析` | 多沙箱后端对比、CSV 上传、可视化 | 数据分析 Agent 实战 |
   119|   119|
   120|   120|---
   121|   121|
   122|   122|### 第八阶段：前端集成
   123|   123|
   124|   124|**目标：** 为 Agent 构建丰富的交互式 UI。
   125|   125|
   126|   126|**前置依赖：** 第二或第三阶段完成（了解 Agent 调用方式即可）。需要 React/TypeScript 基础。
   127|   127|
   128|   128|| 步骤 | Notebook | 核心知识点 | 产出 |
   129|   129||:----:|----------|-----------|------|
   130|   130|| 1 | `langchain/08_前端集成/01_概述与集成库` | `useStream` Hook 架构(后端 stream + 前端 submit)、4 种框架支持(React/Vue/Svelte/Angular)、4 个集成库对比(AI Elements/assistant-ui/CopilotKit/OpenUI)、后端 Python `create_agent` + Checkpointer 配置、前端 TypeScript 类型定义 | 搭建基础聊天 UI |
   131|   131|| 2 | `langchain/08_前端集成/02_消息渲染` | Markdown 渲染流水线(接收→解析→渲染)、ReactMarkdown + SyntaxHighlighter 组件实现、结构化输出渲染(根据 response 类型渲染自定义组件)、推理 Token 折叠展示(useState + conditional render)、流式 Markdown 优化 | 渲染各类 Agent 输出 |
   132|   132|| 3 | `langchain/08_前端集成/03_交互模式` | 分支聊天(editMessage/regenerate/gotoBranch API)、消息队列(queueLength/submit/cancelQueuedMessage)、工具调用 UI(3 种状态卡片 pending/success/error)、人类审批 UI(approve/reject/editAndSubmit)、中断事件处理(stream.interrupts) | 构建完整交互体验 |
   133|   133|| 4 | `langchain/08_前端集成/04_高级流式` | Join/Rejoin(disconnect/rejoin API, 3 种状态 connected/disconnected/resolved)、时间旅行(getStateHistory/goto/resumeFrom + Timeline 组件)、生成式 UI(json-render Catalog/Renderer) | 实现高级 UI 功能 |
   134|   134|| 5 | `deepagents/09_前端集成/01_概述` | Deep Agents 前端架构(coordinator-worker)、`createDeepAgent` 后端、`useStream` Hook、四种核心模式 | 了解 Deep Agents 前端 |
   135|   135|| 6 | `deepagents/09_前端集成/02_沙箱` | IDE 三栏布局(文件树/代码差异/聊天)、四种沙箱作用域(线程/智能体/用户/会话)、FastAPI 文件浏览 API、实时文件同步 | 构建编码 Agent UI |
   136|   136|| 7 | `deepagents/09_前端集成/03_子Agent流式` | SubagentCard 可折叠卡片、进度追踪、合成指示器、状态图标/徽章 | 展示子 Agent 进度 |
   137|   137|| 8 | `deepagents/09_前端集成/04_任务列表` | TodoList 组件(进度条/状态图标/颜色编码) | 展示任务状态 |
   138|   138|
   139|   139|---
   140|   140|
   141|   141|### 第九阶段：生产部署
   142|   142|
   143|   143|**目标：** 将 Agent 投入生产环境，包括部署、测试、安全配置。
   144|   144|
   145|   145|**前置依赖：** 整个学习路径完成。
   146|   146|
   147|   147|| 步骤 | Notebook | 核心知识点 | 产出 |
   148|   148||:----:|----------|-----------|------|
   149|   149|| 1 | `langchain/10_部署与运维/01_部署与监控` | LangSmith 部署 4 步骤(GitHub 仓库→Deployment→Studio 测试→API URL)、Python SDK 调用(get_sync_client + runs.stream)、REST API 调用(curl + X-Api-Key)、LangSmith Tracing 配置、可观测性 4 功能(Trace/Debug/Evaluate/Monitor)、LangSmith Engine 自动监控、LangGraph Studio 可视化调试(断点/状态检查/时间旅行/手动输入) | 能部署和监控 Agent |
   150|   150|| 2 | `langchain/10_部署与运维/02_安全与审批` | 3 类护栏(输入/输出/行为)：内容过滤、速率限制、注入检测、PII 脱敏、合规检查、格式校验、工具白名单、文件权限、审批流程；`interrupt_on` 配置(审批/拒绝/修改后批准)、流式中断处理(stream.interrupts) | 配置生产安全 |
   151|   151|| 3 | `deepagents/07_生产部署/01_生产部署` | 多租户 3 种作用域(Thread/User/Assistant)、Tool 中读取认证信息(runtime.context)、执行环境选型表(StateBackend/FilesystemBackend/StoreBackend/CompositeBackend)、安全护栏(速率限制/错误处理/数据隐私/权限控制)、LangGraph SDK 调用 | 掌握生产部署方案 |
   152|   152|| 4 | `langchain/09_测试/01_测试` | 3 种测试类型对比(单元/集成/评估)、pytest 工具函数测试、Middleware 模拟测试、LangSmith 评估流程(创建数据集→运行→评分)、3 种评估器(LLM 判断/精确匹配/自定义) | 能测试 Agent 质量 |
   153|   153|| 5 | `deepagents/07_生产部署/02_评估标准` | `RubricMiddleware` 工作流程(Mermaid 流程图)、5 种 verdict(satisfied/needs_revision/max_iterations_reached/failed/grader_error)、完整配置参数表、Lipogram 避诗体完整示例、迭代进度观察(rubric_evaluation_start/end 事件) | 自动化质量评估 |
   154|   154|| 6 | `deepagents/07_生产部署/03_发布日志` | Deep Agents 版本更新参考 | 跟踪框架更新 |
   155|   155|
   156|   156|---
   157|   157|
   158|   158|### 第十阶段：Deep Agents Code（编码 Agent）
   159|   159|
   160|   160|**目标：** 了解 Deep Agents Code(dcode) — 基于 Deep Agents SDK 的开源编码 Agent。
   161|   161|
   162|   162|**前置依赖：** 第三阶段完成。
   163|   163|
   164|   164|| 步骤 | Notebook | 核心知识点 | 产出 |
   165|   165||:----:|----------|-----------|------|
   166|   166|| 1 | `deepagents/08_Deep-Agents-Code/01_概述` | dcode 定位、特点(多模型支持/持久记忆/自定义技能/审批控制) | 了解 dcode |
   167|   167|| 2 | `deepagents/08_Deep-Agents-Code/02_配置` | 配置方式、环境变量 | 配置 dcode |
   168|   168|| 3 | `deepagents/08_Deep-Agents-Code/03_提供商` | 多 Provider 支持、切换方式 | 切换模型提供商 |
   169|   169|| 4 | `deepagents/08_Deep-Agents-Code/04_MCP工具` | MCP 工具集成 | 扩展工具集 |
   170|   170|| 5 | `deepagents/08_Deep-Agents-Code/05_记忆与技能` | 持久记忆、自定义技能 | 定制 Agent 行为 |
   171|   171|| 6 | `deepagents/08_Deep-Agents-Code/06_远程沙箱` | 远程沙箱配置、--sandbox 标志 | 隔离执行环境 |
   172|   172|| 7 | `deepagents/08_Deep-Agents-Code/07_子Agent` | 子 Agent 委派 | 并行任务处理 |
   173|   173|| 8 | `deepagents/08_Deep-Agents-Code/08_数据位置` | 数据存储位置 | 了解数据管理 |
   174|   174|
   175|   175|---
   176|   176|
   177|   177|## 目录结构
   178|   178|
   179|   179|```
   180|   180|langchain_study/
   181|   181|├── langchain/                    # LangChain 官方文档笔记 (22篇)
   182|   182|│   ├── 01_入门基础/                 3篇
   183|   183|│   ├── 02_模型与工具/               2篇
   184|   184|│   ├── 03_Agent与RAG/              3篇
   185|   185|│   ├── 04_记忆与上下文/             1篇
   186|   186|│   ├── 05_运行时与流式/             2篇
   187|   187|│   ├── 06_中间件/                   1篇
   188|   188|│   ├── 07_多Agent/                 3篇
   189|   189|│   ├── 08_前端集成/                 4篇
   190|   190|│   ├── 09_测试/                     1篇
   191|   191|│   └── 10_部署与运维/               2篇
   192|   192|│
   193|   193|├── deepagents/                   # Deep Agents 官方文档笔记 (40篇)
   194|   194|│   ├── 01_核心概念/                 4篇
   195|   195|│   ├── 02_模型与配置/               5篇
   196|   196|│   ├── 03_上下文与记忆/             4篇
   197|   197|│   ├── 04_执行模式/                 7篇
   198|   198|│   ├── 05_工具与沙箱/               2篇
   199|   199|│   ├── 06_应用场景/                 3篇
   200|   200|│   ├── 07_生产部署/                 3篇
   201|   201|│   ├── 08_Deep-Agents-Code/         8篇
   202|   202|│   └── 09_前端集成/                 4篇
   203|   203|│
   204|   204|├── .env                          # 环境变量（勿提交）
   205|   205|├── .env.example                  # 环境变量示例
   206|   206|└── README.md                     # 本文件
   207|   207|```
   208|   208|
   209|   209|---
   210|   210|
   211|   211|## 快速索引
   212|   212|
   213|   213|### 按框架查找
   214|   214|
   215|   215|| 框架 | 总篇数 | 推荐起点 |
   216|   216||------|:------:|----------|
   217|   217|| **LangChain** (`langchain/`) | 22 篇 | 入门基础/01_概述与理念 + 02_快速入门 |
   218|   218|| **Deep Agents** (`deepagents/`) | 40 篇 | 核心概念/01_概述 + 02_快速入门 |
   219|   219|
   220|   220|### 按场景查找
   221|   221|
   222|   222|| 你需要... | 推荐阅读 |
   223|   223||-----------|----------|
   224|   224|| 从零搭建 Agent | `langchain/01_入门基础/02_快速入门`、`deepagents/01_核心概念/02_快速入门` |
   225|   225|| 切换模型 Provider | `langchain/02_模型与工具/01_模型与消息`、`deepagents/02_模型与配置/01_模型` |
   226|   226|| 自定义 Agent 行为 | `deepagents/02_模型与配置/02_自定义`、`langchain/06_中间件/01_中间件` |
   227|   227|| 做 RAG 应用 | `langchain/03_Agent与RAG/02_RAG与检索` |
   228|   228|| 构建多 Agent 系统 | `langchain/07_多Agent/01_核心模式`、`langchain/07_多Agent/03_示例` |
   229|   229|| 搭建前端 UI | `langchain/08_前端集成/01_概述与集成库`、`langchain/08_前端集成/03_交互模式` |
   230|   230|| 生产部署 | `langchain/10_部署与运维/01_部署与监控`、`deepagents/07_生产部署/01_生产部署` |
   231|   231|| 添加安全审批 | `langchain/10_部署与运维/02_安全与审批`、`deepagents/04_执行模式/05_人类审批` |
   232|   232|| 测试评估 Agent | `langchain/09_测试/01_测试`、`deepagents/07_生产部署/02_评估标准` |
   233|   233|
   234|   234|---
   235|   235|
   236|   236|## 环境变量
   237|   237|
   238|   238|复制 `.env.example` 为 `.env`，填入你的 API Key：
   239|   239|
   240|   240|```bash
   241|   241|cp .env.example .env
   242|   242|# 然后编辑 .env 填入真实 Key
   243|   243|```
   244|   244|
   245|   245|## 运行 Notebook
   246|   246|
   247|   247|确保安装了依赖：
   248|   248|
   249|   249|```bash
   250|   250|pip install deepagents langchain langchain-community langgraph jupyter python-dotenv
   251|   251|```
   252|   252|
   253|   253|在 VS Code 中直接打开 `.ipynb` 文件运行，或使用：
   254|   254|
   255|   255|```bash
   256|   256|cd G:\ai_code\langchain_study
   257|   257|jupyter notebook
   258|   258|```
   259|   259|