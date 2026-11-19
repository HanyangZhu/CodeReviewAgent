# CodeReviewAgent - 智能代码审查助手

基于 LangChain 1.x 的代码审查智能体，提供结构分析、基础风格检查和 Markdown 报告。

## 工作方式

使用 `create_agent` 构建智能体：模型自主选择工具及参数，程序执行工具并反馈结果，
模型根据结果决定继续调用工具还是输出最终报告。工具调用顺序没有写死。
程序设置 30 个图执行步骤的上限，避免无限循环；此数值不等于模型调用次数。

- `ChatOpenAI`：通过兼容的 Chat Completions 接口连接原有 ModelScope / Qwen 服务。
- `@tool`：把分析函数暴露为模型可调用的工具。
- `create_agent`：管理模型、工具和消息之间的循环。

不再需要 HelloAgents。保留原有 `LLM_*` 配置，无需因为适配器名称而更换模型服务。
模型及服务端必须支持原生工具调用（tool calling）；兼容聊天接口不代表一定支持工具调用。
保留的示例模型是否仍可用、是否开放工具调用，需要用实际服务验证。

## 安装与配置

需要 Python 3.10 或更高版本，建议在独立虚拟环境中安装：

```bash
python -m pip install -r requirements.txt
```

复制 `.env.example` 为 `.env`，填写真实的 `LLM_API_KEY`。
PowerShell：`Copy-Item .env.example .env`；macOS/Linux：`cp .env.example .env`。

| 配置项 | 含义 |
| --- | --- |
| `LLM_MODEL_ID` | 支持工具调用的模型名称 |
| `LLM_API_KEY` | 对应模型服务的密钥 |
| `LLM_BASE_URL` | 模型服务兼容接口地址 |
| `LLM_TIMEOUT` | 单次请求超时秒数，正整数，默认 60 |

已有环境变量优先于 `.env`，Notebook 不覆盖已有配置。不要提交包含真实密钥的 `.env`。
使用外部模型服务时，待审查源码会随请求发送到配置的服务。

## 运行

从项目根目录启动 `jupyter lab`，确保 Notebook 内核工作目录也是项目根目录。
安装依赖后如已有内核运行，请重启内核。

- 快速体验：按顺序运行第 0 部分所有代码单元格。
- 完整审查：按顺序运行第 1–6 部分，第 7 部分为总结；无需先运行快速演示。
- 运行所有单元格会执行两次演示，均会调用模型服务。

完整流程读取 `data/sample_code.py`，由智能体审查后保存到 `outputs/review_report.md`。
保存时自动创建输出目录；已有报告会被覆盖。
如果智能体请求报错、达到步骤上限或返回空报告，请先解决错误并重新运行审查单元格。

## 工具与范围

| 工具 | 功能 |
| --- | --- |
| `quick_analysis` | 快速统计类和函数 |
| `code_analysis` | 统计函数、类、代码行数以及名称列表 |
| `style_check` | 检查行长度和块缩进，非完整 PEP 8 检查 |

函数统计包含普通函数、异步函数及类方法。静态工具解析源码，不执行被审查代码。
潜在 bug、性能和最佳实践建议由模型结合源码及工具结果生成，需要人工核对。

## 项目结构

```text
CodeReviewAgent/
├── .env.example
├── main.ipynb
├── README.md
├── requirements.txt
├── data/sample_code.py
└── outputs/review_report.md
```

示例代码与示例报告保留原内容。示例报告是此前静态核对的结果，不是此次迁移的模型运行结果。
重复用户名、删除首个匹配项、空列表平均年龄的异常行为均保持不变。

## 常见问题

- 提示缺少密钥：在项目根目录的 `.env` 中配置 `LLM_API_KEY`。
- 找不到输入文件：检查内核的当前工作目录。
- 服务拒绝 `tools` 参数：确认模型及服务支持原生工具调用，必要时更新模型配置。
- 达到步骤上限：缩小输入代码或调整提示词，不会自动降级为固定工具流程。

## 参考与来源

- [LangChain 智能体文档](https://docs.langchain.com/oss/python/langchain/agents)
- [ChatOpenAI 适配器文档](https://docs.langchain.com/oss/python/integrations/chat/openai)
- 原作者：[@jjyaoao](https://github.com/jjyaoao)
- [原项目](https://github.com/datawhalechina/Hello-Agents/tree/main/Co-creation-projects/jjyaoao-CodeReviewAgent)

原项目声明采用 MIT 许可证。
