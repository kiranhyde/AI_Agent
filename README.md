# Web-Searching AI Agent
Learning Git Hub
A minimal LangChain-powered agent that can look up fresh information on the
internet and answer questions with citations pulled from Tavily search results.
The project demonstrates how to combine OpenAI models with third-party tools
inside LangChain agents.

## Features
- LangChain agent executor wired to the `OPENAI_FUNCTIONS` agent type
- Tavily search tool for up-to-date, citation-backed answers
- Simple CLI with configurable model, temperature, and search depth
- `.env`-based configuration for API keys

## Requirements
- Python 3.10+
- OpenAI API key (`OPENAI_API_KEY`)
- Tavily API key (`TAVILY_API_KEY`)

## Setup
1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the sample environment file and add your keys:
   ```bash
   cp .env.example .env
   # edit .env and paste your keys
   ```

## Usage
Ask a question directly from the CLI:
```bash
python main.py "What breakthroughs in battery tech were announced this week?"
```

Omit the positional argument to enter an interactive prompt:
```bash
python main.py
# Enter your question: <type question here>
```

Tune the agent without touching code:
```bash
python main.py \
  --model gpt-4o-mini \
  --temperature 0.0 \
  --max-results 8 \
  --verbose \
  "Summarize the latest Mars mission updates"
```

## Project Structure
```
.
├── ai_agent/
│   ├── __init__.py
│   └── agent.py          # Core LangChain agent wrapper
├── main.py               # CLI entry point
├── requirements.txt
└── .env.example
```

## Troubleshooting
- `MissingEnvironmentVariableError`: Confirm `.env` exports both API keys.
- `ModuleNotFoundError`: Re-install dependencies inside the active virtual env.
- `RateLimitError` / `InvalidRequestError`: Check your API quotas and model
  support for the region tied to your key.

## Next Steps
- Add caching for repeated queries.
- Persist agent traces with LangSmith for observability.
- Expand the toolset (e.g., Wikipedia, FireCrawl, custom APIs) for richer
  answers.
