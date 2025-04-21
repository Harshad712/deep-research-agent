# 🧠 Deep Research AI Agent

A lightweight AI agent that performs deep research on any topic using web search and Gemini-powered summarization. Built using [LangGraph](https://docs.langgraph.dev/), [Tavily](https://docs.tavily.com/), and Google Gemini.

## 🚀 Features

- 🌐 Web search powered by Tavily
- 🧠 Summarized answer generation using Gemini Pro
- 🔄 Modular agent-based architecture using LangGraph
- 📦 Easily extensible and configurable

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/deep-research-agent.git
cd deep-research-agent
```

2. **Create virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up your environment variables:**

Create a `.env` file or set these in your system:

```env
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ⚙️ Usage

Run the agent with:

```bash
python main.py
```

Then enter your research question when prompted.

Example:

```bash
📝 Enter your research question: What are the latest breakthroughs in quantum computing?
```

The final answer will be printed and saved to `answer.txt`.

---

## 🧩 Project Structure

```
deep-research-agent/
│
├── agents/
│   ├── researcher.py        # Tavily search logic
│   └── writer.py            # Gemini summarization logic
│
├── main.py                  # LangGraph workflow setup
├── requirements.txt
└── README.md
```

---

## 🛠️ Built With

- [LangGraph](https://docs.langgraph.dev/)
- [Tavily](https://www.tavily.com/)
- [Google Generative AI SDK (Gemini)](https://ai.google.dev/)
- Python 3.10+

