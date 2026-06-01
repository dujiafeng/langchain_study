#!/usr/bin/env python3
"""Generate all 8 Deep-Agents-Code Jupyter notebooks."""
import json, os

OUT = "/mnt/g/ai_code/langchain_study/deepagents/Deep-Agents-Code"
os.makedirs(OUT, exist_ok=True)

BASE_URL = "https://docs.langchain.com/docs/deep-agents/code/"

def md_cell(src):
    return {"cell_type":"markdown","metadata":{},"source":src}

def code_cell(src):
    return {"cell_type":"code","execution_count":None,"metadata":{},"source":src,"outputs":[]}

def mk(meta_title, source_label, doc_slug, cells):
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.12.0"}},
        "cells": cells
    }
    return nb

# ─── 1. 概述 ───────────────────────────────────────────────────────────────
nb1 = mk("01_概述","overview","overview",[
    md_cell(["# 01_概述\n",
             "**来源:** [LangChain Docs — Deep Agents Code 概述](https://docs.langchain.com/docs/deep-agents/code/overview)\n"]),
    md_cell(["## 1. 什么是 Deep Agents Code？\n\n",
             "Deep Agents Code（`dcode`）是一个基于 Deep Agents SDK 构建的开源终端编码 Agent。\n",
             "它支持任意支持工具调用的 LLM，并可在会话中切换提供商或模型。\n\n",
             "主要特性：\n",
             "- **持久记忆** — 跨会话携带上下文\n",
             "- **可定制技能** — 塑造 Agent 的行为\n",
             "- **审批控制** — 门控代码执行\n",
             "- **MCP 工具** — 通过 Model Context Protocol 加载外部工具\n",
             "- **远程沙箱** — 在远程环境而非本地执行工具\n",
             "- **子 Agent** — 将任务委托给专门的子 Agent"]),
    md_cell(["## 2. 快速开始\n\n",
             "```bash\n# 一键安装并启动\ncurl -LsSf https://langch.in/dcode | bash\n```\n\n",
             "添加提供商凭据后，即可向 Agent 下达任务：\n",
             "```bash\n# 创建一个 Python 脚本打印 \"Hello, World!\"\ndcode\n```"]),
    md_cell(["## 3. 内置工具一览\n\n",
             "| 工具 | 描述 | 人工审批 |\n|------|------|---------|\n| `ls` | 列出文件和目录 | - |\n| `read_file` | 读取文件内容 | - |\n| `write_file` | 创建或覆盖文件 | 需要 |\n| `edit_file` | 对现有文件进行定向编辑 | 需要 |\n| `glob` | 查找匹配模式的文件 | - |\n| `grep` | 跨文件搜索文本模式 | - |\n| `execute` | 执行 Shell 命令 | 需要 |\n| `web_search` | 使用 Tavily 搜索网页 | 需要 |\n| `fetch_url` | 获取网页并转为 Markdown | 需要 |\n| `task` | 将工作委派给子 Agent | 需要 |\n| `ask_user` | 向用户提问 | - |\n| `compact_conversation` | 压缩对话历史 | 混合 |\n| `write_todos` | 创建和管理任务列表 | - |\n\n> **注意：** 具有潜在破坏性的操作需要用户审批后方可执行。",
             "可通过 `Shift+Tab` 切换自动审批模式，或使用 `-y` / `--auto-approve` 标志启动。"]),
    md_cell(["## 4. 命令参考\n\n",
             "```bash\n# 使用特定 Agent 配置\ndcode --agent mybot\n\n# 使用特定模型 (provider:model 格式)\ndcode --model anthropic:claude-opus-4-7\n\n# 使用自动审批模式\ndcode -y\n\n# 非交互模式\ndcode -n \"Summarize this repo\"\n```"]),
    md_cell(["## 5. 启用追踪（可选）\n\n",
             "将以下内容添加到 `~/.deepagents/.env` 或导出环境变量：\n",
             "```bash\nLANGSMITH_TRACING=true\nLANGSMITH_API_KEY=lsv2_pt_...\nLANGSMITH_PROJECT=deepagents-code\n```"]),
    md_cell(["## 参考\n\n",
             "- [配置文档](https://docs.langchain.com/docs/deep-agents/code/configuration)\n",
             "- [提供商文档](https://docs.langchain.com/docs/deep-agents/code/providers)\n",
             "- [MCP 工具文档](https://docs.langchain.com/docs/deep-agents/code/mcp-tools)\n",
             "- [GitHub — Deep Agents Code](https://github.com/langchain-ai/deep-agents)"])
])

# ─── 2. 配置 ───────────────────────────────────────────────────────────────
nb2 = mk("02_配置","configuration","configuration",[
    md_cell(["# 02_配置\n",
             "**来源:** [LangChain Docs — Deep Agents Code 配置](https://docs.langchain.com/docs/deep-agents/code/configuration)\n"]),
    md_cell(["## 1. 配置文件结构\n\n",
             "Deep Agents Code 的配置存储在 `~/.deepagents/` 目录下：\n\n",
             "| 文件 | 格式 | 用途 |\n|------|------|------|\n| `config.toml` | TOML | 模型默认值、提供商设置、构造函数参数、主题等 |\n| `.env` | Dotenv | 全局 API 密钥和 secrets |\n| `hooks.json` | JSON | 生命周期事件订阅 |\n| `.mcp.json` | JSON | MCP 服务器定义 |"]),
    md_cell(["## 2. 提供商凭据管理\n\n",
             "有两种方式设置凭据：\n\n",
             "**推荐：使用 `/auth` 命令**\n",
             "```bash\n# 在会话中打开凭据管理器\n/auth\n```\n\n",
             "**环境变量方式（适用于 CI/CD）：**\n",
             "```python\n# 在 ~/.deepagents/.env 中设置\nANTHROPIC_API_KEY = \"sk-ant-...\"\nOPENAI_API_KEY = \"sk-...\"\n\n# 也可以使用 DEEPAGENTS_CODE_ 前缀隔离作用域\n# DEEPAGENTS_CODE_OPENAI_API_KEY = \"sk-...\"\n```"]),
    md_cell(["## 3. 环境变量加载顺序\n\n",
             "```text\n# 优先级：shell 环境 > 项目 .env > 全局 .env\n# 已设置的 shell 变量不会被覆盖\n```\n\n",
             "两个 `.env` 文件在启动时被加载：\n",
             "1. **项目 `.env`** — 当前工作目录下的 `.env` 文件\n",
             "2. **全局 `~/.deepagents/.env`** — 所有项目的共享后备文件"]),
    md_cell(["## 4. 启用 Web 搜索（Tavily）\n\n",
             "```bash\n# 在 ~/.deepagents/.env 中添加\nTAVILY_API_KEY = \"tvly-...\"\n\n# 或使用前缀隔离\nDEEPAGENTS_CODE_TAVILY_API_KEY = \"tvly-...\"\n\n# 在会话中重新加载\n/reload\n```"]),
    md_cell(["## 5. config.toml 详解\n\n",
             "```toml\n# 默认和最近使用的模型\n[models]\ndefault = \"ollama:qwen3:4b\"\nrecent = \"google_genai:gemini-3.5-flash\"\n\n# 提供商配置\n[models.providers.ollama]\nmodels = [\"qwen3:4b\", \"llama3\"]\nbase_url = \"http://localhost:11434\"\n\n[models.providers.ollama.params]\ntemperature = 0\nnum_ctx = 8192\n\n# 每个模型的参数覆盖\n[models.providers.ollama.params.\"qwen3:4b\"]\ntemperature = 0.5\nnum_ctx = 4000\n```"]),
    md_cell(["## 参考\n\n",
             "- [提供商文档](https://docs.langchain.com/docs/deep-agents/code/providers)\n",
             "- [MCP 工具文档](https://docs.langchain.com/docs/deep-agents/code/mcp-tools)\n",
             "- [环境变量参考](https://docs.langchain.com/docs/deep-agents/code/environment-variables)"])
])

# ─── 3. 提供商 ───────────────────────────────────────────────────────────────
nb3 = mk("03_提供商","providers","providers",[
    md_cell(["# 03_提供商\n",
             "**来源:** [LangChain Docs — Deep Agents Code 模型提供商](https://docs.langchain.com/docs/deep-agents/code/providers)\n"]),
    md_cell(["## 1. 支持的提供商\n\n",
             "Deep Agents Code 支持所有 LangChain 兼容的聊天模型提供商。\n",
             "以下提供商内置支持（安装对应 extras 即可）：\n\n",
             "| 提供商 | 包名 | 凭据环境变量 | 模型配置 |\n|--------|------|-------------|---------|\n| OpenAI | `langchain-openai` | `OPENAI_API_KEY` | ✅ |\n| Azure OpenAI | `langchain-openai` | `AZURE_OPENAI_API_KEY` | ✅ |\n| Anthropic | `langchain-anthropic` | `ANTHROPIC_API_KEY` | ✅ |\n| Google Gemini | `langchain-google-genai` | `GOOGLE_API_KEY` | ✅ |\n| AWS Bedrock | `langchain-aws` | `AWS_ACCESS_KEY_ID` | ✅ |\n| Ollama | `langchain-ollama` | (可选) | ❌ |\n| Groq | `langchain-groq` | `GROQ_API_KEY` | ✅ |\n| DeepSeek | `langchain-deepseek` | `DEEPSEEK_API_KEY` | ✅ |\n| xAI | `langchain-xai` | `XAI_API_KEY` | ✅ |\n| Perplexity | `langchain-perplexity` | `PERPLEXITY_API_KEY` | ✅ |\n| OpenRouter | `langchain-openrouter` | `OPENROUTER_API_KEY` | ✅ |\n| LiteLLM | `langchain-litellm` | 依提供商而定 | ❌ |"]),
    md_cell(["## 2. 安装提供商包\n\n",
             "```bash\n# 安装时指定 extras\nDEEPAGENTS_EXTRAS=\"baseten,groq\" curl -LsSf https://langch.in/dcode | bash\n\n# 或使用 uv 工具安装\nuv tool install 'deepagents-code[baseten,groq]'\n\n# 后续添加包\nuv tool install deepagents-code --with langchain-ollama\n\n# 安装所有提供商\nuv tool install 'deepagents-code[anthropic,baseten,bedrock,...]'\n```"]),
    md_cell(["## 3. 切换模型\n\n",
             "```bash\n# 交互式切换\n/model\n\n# 直接指定模型\n/model anthropic:claude-opus-4-7\n\n# 启动时指定\ndcode --model openai:gpt-5.5\n\n# 设置默认模型\n/model --default anthropic:claude-opus-4-7\n\n# 清除默认模型\n/model --default --clear\n```"]),
    md_cell(["## 4. 模型解析顺序\n\n",
             "```text\n1. --model 标志（最高优先级）\n2. [models].default 配置\n3. [models].recent 配置（/model 自动写入）\n4. 环境自动检测：OPENAI_API_KEY → ANTHROPIC_API_KEY → GOOGLE_API_KEY → GOOGLE_CLOUD_PROJECT\n```"]),
    md_cell(["## 5. 模型参数\n\n",
             "```python\n# 通过 --model-params 传递额外参数（最高优先级，仅本次会话）\ndcode --model openai:gpt-5.5 --model-params '{\"reasoning\": {\"effort\": \"high\"}}'\n\n# 或通过 config.toml 持久设置\n# [models.providers.anthropic.params]\n# thinking = { type = \"enabled\", budget_tokens = 10000 }\n# max_tokens = 16000\n```"]),
    md_cell(["## 参考\n\n",
             "- [配置文档](https://docs.langchain.com/docs/deep-agents/code/configuration)\n",
             "- [LangChain 模型集成](https://python.langchain.com/docs/integrations/chat/)\n",
             "- [自定义提供商](https://docs.langchain.com/docs/deep-agents/code/providers#arbitrary-providers)"])
])

# ─── 4. MCP工具 ───────────────────────────────────────────────────────────────
nb4 = mk("04_MCP工具","mcp-tools","mcp-tools",[
    md_cell(["# 04_MCP工具\n",
             "**来源:** [LangChain Docs — Deep Agents Code MCP 工具](https://docs.langchain.com/docs/deep-agents/code/mcp-tools)\n"]),
    md_cell(["## 1. 什么是 MCP？\n\n",
             "MCP（Model Context Protocol）允许你通过外部服务器扩展 Deep Agents Code 的工具集——\n",
             "文件系统、API、数据库等，而无需修改 Agent 本身。\n\n",
             "Deep Agents Code 在启动时自动发现 MCP 服务器，加载其工具，\n",
             "使其与内置工具一起供 Agent 使用。"]),
    md_cell(["## 2. 快速开始：添加 MCP 服务器\n\n",
             "### 创建配置文件\n\n",
             "**用户级别（所有项目均可用）：**\n",
             "```json\n{\n    \"mcpServers\": {\n        \"docs-langchain\": {\n            \"type\": \"http\",\n            \"url\": \"https://docs.langchain.com/mcp\"\n        }\n    }\n}\n```\n\n",
             "**项目级别：** 在项目根目录下放置 `.mcp.json` 文件\n",
             "**项目隐藏级别：** `.deepagents/.mcp.json`"]),
    md_cell(["## 3. 自动发现位置\n\n",
             "| 优先级 | 位置 | 作用域 |\n|--------|------|--------|\n| 1 (低) | `~/.deepagents/.mcp.json` | 用户级别，所有项目 |\n| 2 | `<项目>/.deepagents/.mcp.json` | 项目级别，`.deepagents` 子目录 |\n| 3 (高) | `<项目>/.mcp.json` | 项目级别，根目录（兼容 Claude Code） |\n\n",
             "支持 `--mcp-config PATH` 添加显式配置文件（最高优先级），\n",
             "以及 `--no-mcp` 禁用所有 MCP 加载。"]),
    md_cell(["## 4. 配置格式\n\n",
             "### stdio 服务器（默认）\n",
             "```json\n{\n  \"mcpServers\": {\n    \"filesystem\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@modelcontextprotocol/server-filesystem\", \"/tmp\"],\n      \"env\": {}\n    }\n  }\n}\n```\n\n",
             "### SSE 和 HTTP 服务器\n",
             "```json\n{\n  \"mcpServers\": {\n    \"remote-api\": {\n      \"type\": \"sse\",\n      \"url\": \"https://api.example.com/mcp\",\n      \"headers\": { \"Authorization\": \"Bearer your-token\" }\n    }\n  }\n}\n```"]),
    md_cell(["## 5. 工具过滤\n\n",
             "```json\n{\n  \"mcpServers\": {\n    \"filesystem\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@modelcontextprotocol/server-filesystem\", \"/tmp\"],\n      \"allowedTools\": [\"read_file\", \"list_directory\"]\n    },\n    \"github\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@modelcontextprotocol/server-github\"],\n      \"env\": { \"GITHUB_TOKEN\": \"ghp_...\" },\n      \"disabledTools\": [\"delete_repository\"]\n    }\n  }\n}\n```\n\n",
             "`allowedTools` 和 `disabledTools` 互斥，支持 `fnmatch` 通配符。"]),
    md_cell(["## 6. OAuth 登录\n\n",
             "对于需要 OAuth 的远程 MCP 服务器：\n",
             "```json\n{\n  \"mcpServers\": {\n    \"linear\": {\n      \"type\": \"http\",\n      \"url\": \"https://mcp.linear.app/mcp\",\n      \"auth\": \"oauth\"\n    }\n  }\n}\n```\n\n",
             "```bash\n# 运行 OAuth 登录流程\ndcode mcp login linear\n```"]),
    md_cell(["## 参考\n\n",
             "- [LangSmith Remote MCP](https://docs.smith.langchain.com/how_to_guides/mcp)\n",
             "- [MCP 协议规范](https://modelcontextprotocol.io/)\n",
             "- [项目信任机制](https://docs.langchain.com/docs/deep-agents/code/mcp-tools#project-level-trust)"])
])

# ─── 5. 记忆与技能 ───────────────────────────────────────────────────────────────
nb5 = mk("05_记忆与技能","memory-and-skills","memory-and-skills",[
    md_cell(["# 05_记忆与技能\n",
             "**来源:** [LangChain Docs — Deep Agents Code 记忆与技能](https://docs.langchain.com/docs/deep-agents/code/memory-and-skills)\n"]),
    md_cell(["## 1. 两种定制方式\n\n",
             "在 Deep Agents Code 中有两种定制 Agent 的方式：\n\n",
             "- **记忆（Memory）** — `AGENTS.md` 文件和自动保存的记忆，跨会话持久化。\n",
             "  用于编码风格、偏好和学到的约定。\n",
             "- **技能（Skills）** — 全局和项目级别的上下文、约定、指南。\n",
             "  用于执行特定任务时的上下文。"]),
    md_cell(["## 2. 自动记忆\n\n",
             "Agent 在 `~/.deepagents/<agent_name>/memories/` 中自动存储信息：\n",
             "```text\n~/.deepagents/backend-dev/memories/\n├── api-conventions.md\n├── database-schema.md\n└── deployment-process.md\n```\n\n",
             "工作流程：\n",
             "1. **Research** — 在开始任务前搜索相关记忆\n",
             "2. **Response** — 执行时不确时检查记忆\n",
             "3. **Learning** — 自动保存新信息供将来使用"]),
    md_cell(["## 3. AGENTS.md 文件\n\n",
             "提供始终在会话启动时加载的持久上下文：\n\n",
             "- **全局：** `~/.deepagents/<agent_name>/AGENTS.md` — 每次会话加载\n",
             "- **项目：** `.deepagents/AGENTS.md` — 从该项目中运行时加载\n\n",
             "```markdown\n# ~/.deepagents/agent/AGENTS.md（全局）\n## 我的编码风格\n- 使用 snake_case 命名\n- 包含类型注解\n- 每个函数都写 docstring\n```"]),
    md_cell(["## 4. 技能（Skills）\n\n",
             "技能是可复用的 Agent 能力，提供专门的工作流和领域知识。\n\n",
             "```bash\n# 创建技能\n# 用户级别（~/.deepagents/<agent>/skills/）\ndcode skills create test-skill\n\n# 项目级别（.deepagents/skills/）\ndcode skills create test-skill --project\n```\n\n",
             "这将生成：\n",
             "```text\nskills/\n└── test-skill/\n    └── SKILL.md\n```"]),
    md_cell(["## 5. 技能发现路径\n\n",
             "```text\n~/.deepagents/<agent_name>/skills/\n~/.agents/skills/\n.deepagents/skills/\n.agents/skills/\n~/.claude/skills/          （实验性）\n.claude/skills/            （实验性）\n```"]),
    md_cell(["## 6. 调用技能\n\n",
             "```bash\n# 会话中直接调用\n/skill:code-review\n/skill:code-review review the auth module\n\n# 启动时加载技能\ndcode --skill code-review\ndcode --skill code-review -m 'review the auth module'\n\n# 列出技能\ndcode skills list\ndcode skills list --project\ndcode skills info test-skill\n```"]),
    md_cell(["## 参考\n\n",
             "- [Agent Skills 标准](https://github.com/langchain-ai/agent-skills-spec)\n",
             "- [Vercel Skills CLI](https://www.npmjs.com/package/@vercel/skills)\n",
             "- [SDK 记忆文档](https://docs.langchain.com/docs/deep-agents/sdk/memory)"])
])

# ─── 6. 远程沙箱 ───────────────────────────────────────────────────────────────
nb6 = mk("06_远程沙箱","remote-sandboxes","remote-sandboxes",[
    md_cell(["# 06_远程沙箱\n",
             "**来源:** [LangChain Docs — Deep Agents Code 远程沙箱](https://docs.langchain.com/docs/deep-agents/code/remote-sandboxes)\n"]),
    md_cell(["## 1. 沙箱模式简介\n\n",
             "Deep Agents Code 采用 **沙箱即工具** 模式：\n",
             "- `dcode` 进程（LLM 循环、记忆、工具调度）在本地运行\n",
             "- Agent 工具调用（`read_file`、`write_file`、`execute` 等）目标指向远程沙箱\n\n",
             "支持的沙箱提供商：\n",
             "| 提供商 | 安装命令 | 凭据环境变量 |\n|--------|---------|-------------|\n| LangSmith | 默认内置 | `LANGSMITH_API_KEY` |\n| Daytona | `'deepagents-code[daytona]'` | `DAYTONA_API_KEY` |\n| Modal | `'deepagents-code[modal]'` | Modal 设置 |\n| Runloop | `'deepagents-code[runloop]'` | `RUNLOOP_API_KEY` |\n| AgentCore | `'deepagents-code[agentcore]'` | AWS 凭据 |"]),
    md_cell(["## 2. 安装沙箱依赖\n\n",
             "```bash\n# 安装所有沙箱提供商\nuv tool install 'deepagents-code[all-sandboxes]'\n\n# 或单独安装\nuv tool install 'deepagents-code[daytona]'\nuv tool install 'deepagents-code[modal]'\nuv tool install 'deepagents-code[runloop]'\n```"]),
    md_cell(["## 3. 设置凭据\n\n",
             "```bash\n# LangSmith\nexport LANGSMITH_API_KEY=\"lsv2_...\"\n\n# Daytona\nexport DAYTONA_API_KEY=\"dpa_...\"\n\n# Runloop\nexport RUNLOOP_API_KEY=\"rl_...\"\n\n# AgentCore (AWS Bedrock)\nexport AWS_ACCESS_KEY_ID=\"your-key\"\nexport AWS_SECRET_ACCESS_KEY=\"your-secret\"\nexport AWS_REGION=\"us-west-2\"\n```"]),
    md_cell(["## 4. 使用沙箱\n\n",
             "```bash\n# 使用 LangSmith 沙箱\ndcode --sandbox langsmith\n\n# 使用 Daytona 沙箱\ndcode --sandbox daytona\n\n# 使用已存在的沙箱（跳过创建和清理）\ndcode --sandbox runloop --sandbox-id dbx_abc123\n\n# 使用设置脚本\ndcode --sandbox modal --sandbox-setup ./setup.sh\n```"]),
    md_cell(["## 5. 沙箱标志和默认工作目录\n\n",
             "| 提供商 | 默认工作目录 |\n|--------|-------------|\n| LangSmith | `/root` |\n| Daytona | `/home/daytona` |\n| Modal | `/workspace` |\n| Runloop | `/home/user` |\n| AgentCore | `/tmp` |\n\n",
             "```bash\n# 示例：创建新 Daytona 沙箱\n# dcode --sandbox daytona\n\n# 示例：重用现有沙箱\n# dcode --sandbox runloop --sandbox-id dbx_abc123\n\n# 示例：创建后运行设置脚本\n# dcode --sandbox modal --sandbox-setup ./setup.sh\n```"]),
    md_cell(["## 6. 设置脚本示例\n\n",
             "```bash\n#!/bin/bash\nset -e\n\n# 克隆仓库\ngit clone https://github.com/username/repo.git $HOME/workspace\ncd $HOME/workspace\n\n# 持久化环境变量\ncat >> ~/.bashrc <<'EOF'\nexport OPENAI_API_KEY=\"${OPENAI_API_KEY}\"\ncd $HOME/workspace\nEOF\nsource ~/.bashrc\n```\n\n",
             "> **安全提示：** 沙箱隔离了代码执行，但 Agent 仍可能受到提示注入攻击。\n",
             "请使用人工审批、短生命周期 secrets 和受信设置脚本。"]),
    md_cell(["## 参考\n\n",
             "- [沙箱架构](https://docs.langchain.com/docs/deep-agents/code/sandboxes)\n",
             "- [安全考虑](https://docs.langchain.com/docs/deep-agents/code/sandboxes#security-considerations)\n",
             "- [LangSmith 沙箱](https://docs.smith.langchain.com/how_to_guides/sandboxes)"])
])

# ─── 7. 子Agent ───────────────────────────────────────────────────────────────
nb7 = mk("07_子Agent","subagents","subagents",[
    md_cell(["# 07_子Agent\n",
             "**来源:** [LangChain Docs — Deep Agents Code 子 Agent](https://docs.langchain.com/docs/deep-agents/code/subagents)\n"]),
    md_cell(["## 1. 什么是子 Agent？\n\n",
             "子 Agent（Subagents）允许你将专门任务委托给独立的 Agent 实例。\n",
             "每个子 Agent 生活在自己的文件夹中，通过 `AGENTS.md` 文件定义：\n\n",
             "```text\n.deepagents/agents/{subagent-name}/AGENTS.md          # 项目级别\n~/.deepagents/{agent}/agents/{subagent-name}/AGENTS.md # 用户级别\n```\n\n",
             "> **注意：** 目前 Deep Agents Code 仅支持同步子 Agent。异步子 Agent 暂不可用。"]),
    md_cell(["## 2. 文件格式\n\n",
             "子 Agent 的 `AGENTS.md` 文件使用 YAML 前言 + Markdown 正文：\n\n",
             "```yaml\n---\nname: researcher\ndescription: Research topics on the web before writing content\nmodel: anthropic:claude-haiku-4-5-20251001\n---\n\nYou are a research assistant with access to web search.\n\n## Your Process\n1. Search for relevant information\n2. Summarize findings clearly\n```\n\n",
             "| 字段 | 必需 | 描述 |\n|------|------|------|\n| `name` | ✅ | 子 Agent 名称 |\n| `description` | ✅ | 描述，用于触发委托 |\n| `model` | ❌ | 覆盖主 Agent 的模型（`provider:model` 格式） |"]),
    md_cell(["## 3. 优先级规则\n\n",
             "```text\n用户级别：~/.deepagents/{agent}/agents/ （较低优先级）\n项目级别：.deepagents/agents/         （较高优先级）\n```\n\n",
             "项目级别的子 Agent 会覆盖同名的用户级别子 Agent。"]),
    md_cell(["## 4. 示例：成本高效子 Agent\n\n",
             "为简单委托任务使用更便宜、更快的模型：\n\n",
             "```yaml\n# ~/.deepagents/agent/agents/general-purpose/AGENTS.md\n---\nname: general-purpose\ndescription: General-purpose agent for research and multi-step tasks\nmodel: anthropic:claude-haiku-4-5-20251001\n---\n\nYou are a general-purpose assistant. Complete the task efficiently\nand return a concise summary.\n```\n\n",
             "这将覆盖内置的通用子 Agent，将所有委托任务路由到更便宜的模型。"]),
    md_cell(["## 5. 使用子 Agent\n\n",
             "```bash\n# 进入 dcode 会话后，Agent 会根据任务描述自动决定是否委托\n# 给子 Agent。你也可以通过 /task 工具手动触发。\n\n# 示例：要求 Agent 研究一个主题\n# \"Research the latest Python 3.13 features and summarize them\"\n# → Agent 可能将研究部分委托给 researcher 子 Agent\n```"]),
    md_cell(["## 参考\n\n",
             "- [SubAgent SDK 文档](https://docs.langchain.com/docs/deep-agents/sdk/subagents)\n",
             "- [配置文档](https://docs.langchain.com/docs/deep-agents/code/configuration)\n",
             "- [Deep Agents SDK](https://docs.langchain.com/docs/deep-agents/sdk)"])
])

# ─── 8. 数据位置 ───────────────────────────────────────────────────────────────
nb8 = mk("08_数据位置","data-locations","data-locations",[
    md_cell(["# 08_数据位置\n",
             "**来源:** [LangChain Docs — Deep Agents Code 数据位置](https://docs.langchain.com/docs/deep-agents/code/data-locations)\n"]),
    md_cell(["## 1. 目录结构概览\n\n",
             "Deep Agents Code 将数据存储在两大目录层级中：\n\n",
             "```text\n~/.deepagens/          # Deep Agents 特定数据\n~/.agents/             # 工具无关数据（跨 AI CLI 工具共享）\n<project>/             # 项目级别（Git 仓库根目录）\n```"]),
    md_cell(["## 2. 详细目录结构\n\n",
             "```text\n~/.deepagens/\n├── .state/                    # 自动管理的每机器状态\n│   ├── sessions.db            # SQLite 对话检查点数据库\n│   ├── history.jsonl          # 命令输入历史\n│   └── ...\n└── {agent}/                   # 每 Agent 目录（默认: \"agent\"）\n    ├── AGENTS.md              # 用户对 Agent 指令的定制\n    ├── skills/                # 用户级别技能\n    │   └── {skill-name}/\n    │       └── SKILL.md\n    └── agents/                # 自定义子 Agent\n        └── {subagent-name}/\n            └── AGENTS.md\n\n~/.agents/                     # 工具无关别名\n└── skills/\n    └── {skill-name}/\n        └── SKILL.md\n\n{project}/\n├── AGENTS.md                  # 项目指令\n└── .deepagents/\n    ├── AGENTS.md\n    ├── skills/\n    └── agents/\n```"]),
    md_cell(["## 3. 数据位置对照表\n\n",
             "| 数据 | 位置 | 读写 | 备注 |\n|------|------|------|------|\n| 会话 | `~/.deepagents/.state/sessions.db` | R/W | SQLite 检查点数据库 |\n| 输入历史 | `~/.deepagents/.state/history.jsonl` | R/W | JSON lines，上下箭头召回 |\n| 基础指令 | 包内 `default_agent_prompt.md` | R | 不可变，随升级更新 |\n| 用户定制 | `~/.deepagents/{agent}/AGENTS.md` | R/W | 追加到基础指令后 |\n| 项目指令 | `.deepagents/AGENTS.md` 或 `AGENTS.md` | R/W | 两者都存在时都加载 |\n| 用户技能 | `~/.deepagents/{agent}/skills/` | R/W | Agent 特定技能 |\n| 共享技能 | `~/.agents/skills/` | R | 跨 CLI 工具 |\n| 项目技能 | `.deepagents/skills/` | R | 项目范围 |\n| 自定义子 Agent | `~/.deepagents/{agent}/agents/` | R/W | 用户定义 |\n| 项目子 Agent | `.deepagents/agents/` | R | 项目定义 |"]),
    md_cell(["## 4. 优先级规则\n\n",
             "**技能优先级（从低到高）：**\n",
             "```text\n1. ~/.deepagents/{agent}/skills/     — 用户 Deep Agents\n2. ~/.agents/skills/                — 用户工具无关\n3. .deepagents/skills/              — 项目 Deep Agents\n4. .agents/skills/                  — 项目工具无关（最高）\n```\n\n",
             "**子 Agent 优先级（从低到高）：**\n",
             "```text\n1. ~/.deepagents/{agent}/agents/    — 用户级别\n2. .deepagents/agents/              — 项目级别（最高）\n```\n\n",
             "**指令：** 所有来源都会被组合（不覆盖）：\n",
             "```text\n包基础提示（始终加载）\n+ ~/.deepagents/{agent}/AGENTS.md（追加）\n+ .deepagents/AGENTS.md（追加）\n+ AGENTS.md（项目根目录，追加）\n```"]),
    md_cell(["## 5. 清理操作\n\n",
             "| 操作 | 命令 |\n|------|------|\n| 重置所有数据 | `rm -rf ~/.deepagents` |\n| 清除会话 | `rm ~/.deepagents/.state/sessions.db*` |\n| 清除输入历史 | `rm ~/.deepagents/.state/history.jsonl` |\n| 清除存储的 API 密钥 | `rm ~/.deepagents/.state/auth.json` |\n| 清除 MCP OAuth 令牌 | `rm -rf ~/.deepagents/.state/mcp-tokens` |\n| 重新运行首次引导 | `rm ~/.deepagents/.state/onboarding_complete` |\n| 重置 Agent 指令 | `dcode agents reset --agent {name}` |\n| 删除技能 | `rm -rf ~/.deepagents/{agent}/skills/{skill-name}` |"]),
    md_cell(["## 6. `.deepagents` vs `.agents`\n\n",
             "| 目录 | 用途 | 使用场景 |\n|------|------|---------|\n| `.deepagents/` | Deep Agents Code 特定 | 使用 Deep Agents 特定特性的技能和配置 |\n| `.agents/` | 工具无关 | 希望跨不同 AI CLI 工具共享的技能 |\n\n",
             "> 使用 `.agents/skills/` 存放可与任意 AI 编码助手协作的技能；\n",
             "> 使用 `.deepagents/skills/` 存放依赖 Deep Agents 特定工具或约定的技能。"]),
    md_cell(["## 参考\n\n",
             "- [配置文档](https://docs.langchain.com/docs/deep-agents/code/configuration)\n",
             "- [记忆与技能文档](https://docs.langchain.com/docs/deep-agents/code/memory-and-skills)\n",
             "- [子 Agent 文档](https://docs.langchain.com/docs/deep-agents/code/subagents)"])
])

# ─── Write all notebooks ────────────────────────────────────────────────────
notebooks = [
    ("01_概述.ipynb", nb1),
    ("02_配置.ipynb", nb2),
    ("03_提供商.ipynb", nb3),
    ("04_MCP工具.ipynb", nb4),
    ("05_记忆与技能.ipynb", nb5),
    ("06_远程沙箱.ipynb", nb6),
    ("07_子Agent.ipynb", nb7),
    ("08_数据位置.ipynb", nb8),
]

created = []
for fname, nb in notebooks:
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    created.append(path)
    print(f"Created: {path}")

print("\n--- All done ---")
for p in created:
    print(p)
