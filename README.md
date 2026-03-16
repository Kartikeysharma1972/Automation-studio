# 🤖 Automation Studio

AI-powered workflow automation platform that runs locally using open-source models.

## ✨ Features

- 🧠 **AI Agents** - Autonomous agents for research, analysis, and content creation
- ⚡ **Local Processing** - 100% offline, no API costs, complete data privacy
- 🔧 **Tool Integration** - File operations, text processing, data analysis
- 🎯 **Workflow Builder** - Visual workflow creation and execution
- 💾 **Vector Memory** - Semantic search and knowledge management
- 🔄 **Event-Driven** - Automated triggers and scheduling

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+ (optional for frontend)
- Ollama with local models

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Kartikeysharma1972/Automation-studio.git
cd Automation-studio
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup Ollama models**
```bash
# Install Ollama from https://ollama.ai
ollama pull deepseek-coder
ollama pull nomic-embed-text
```

4. **Start the application**
```bash
python main.py
```

5. **Access the platform**
- API: http://localhost:8000
- Health Check: http://localhost:8000/health
- API Docs: http://localhost:8000/docs

## 🛠️ Usage Examples

### AI Agent Example
```python
from app import AIAgent

# Initialize agent
agent = AIAgent(model="deepseek-coder")

# Execute task
result = agent.execute("Analyze this data and provide insights")
print(result)
```

### Automation Workflow
```python
from agent import AutomationAgent

# Create automation agent
automation = AutomationAgent()

# Process tasks
result = automation.process_task("Generate monthly report")
print(result)

# Use tools
analysis = automation.use_tool("data_analysis", "sales_data.csv")
print(analysis)
```

## 🧠 Available AI Agents

- **Research Assistant** - Information gathering and analysis
- **Data Analyst** - Data processing and insights generation  
- **Content Writer** - Content creation and editing

## 🔧 Available Tools

- **Text Processing** - Summarization, extraction, analysis
- **File Operations** - Read, write, process documents
- **Data Analysis** - CSV processing, statistics
- **Memory Management** - Vector storage and search

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend API   │    │   AI Engine     │
│   (Optional)    │◄──►│   (FastAPI)     │◄──►│   (Ollama)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Vector Memory  │
                       │  (ChromaDB)     │
                       └─────────────────┘
```

## 🌟 Key Benefits

- 💰 **Cost Effective** - No API subscriptions, completely free
- 🔒 **Privacy First** - 100% local processing, data never leaves your machine
- 🚀 **High Performance** - Optimized for local execution
- 🧩 **Modular** - Easy to extend with new agents and tools
- 🎯 **Production Ready** - Built with enterprise-grade architecture

## 📋 Tech Stack

- **Backend**: FastAPI, Python, SQLAlchemy
- **AI Engine**: Ollama, DeepSeek-Coder, Nomic-Embed
- **Vector Database**: ChromaDB
- **Frontend**: Next.js, React (Optional)
- **Database**: SQLite, PostgreSQL (Optional)

## 🔧 Configuration

Create a `.env` file:
```env
OLLAMA_BASE_URL=http://localhost:11434
DEFAULT_MODEL=deepseek-coder
EMBEDDING_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./automation.db
```

## 📖 API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /agent/execute` - Execute AI agent task
- `POST /workflow/create` - Create workflow
- `GET /memory/search` - Search vector memory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) - Local LLM inference
- [FastAPI](https://fastapi.tiangolo.com) - Modern web framework
- [ChromaDB](https://www.trychroma.com) - Vector database

## 📞 Support

If you have any questions or need support, please open an issue on GitHub.

---

**Built with ❤️ for the AI automation community**
