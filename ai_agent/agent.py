"""LangChain-powered web-search agent."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, AgentType, initialize_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

load_dotenv()


class MissingEnvironmentVariableError(ValueError):
  """Raised when a required environment variable is missing."""


def _require_env(var_name: str) -> None:
  """Ensure a required environment variable is present."""
  if os.getenv(var_name):
    return
  raise MissingEnvironmentVariableError(
      f"Set the {var_name} environment variable before using the agent.")


@dataclass
class AgentConfig:
  """Runtime configuration for the AI agent."""

  model: str = "gpt-4o-mini"
  temperature: float = 0.1
  max_search_results: int = 4
  verbose: bool = False


class WebSearchAgent:
  """AI agent that searches the web and answers questions."""

  def __init__(self, config: AgentConfig | None = None) -> None:
    self._config = config or AgentConfig()
    _require_env("OPENAI_API_KEY")
    _require_env("TAVILY_API_KEY")
    self._llm = self._build_llm()
    self._agent = self._build_agent()

  def _build_llm(self) -> ChatOpenAI:
    """Return the language model used by the agent."""
    return ChatOpenAI(
        model=self._config.model,
        temperature=self._config.temperature)

  def _build_agent(self) -> AgentExecutor:
    """Wire up the LangChain agent executor."""
    tools = [
        TavilySearchResults(max_results=self._config.max_search_results)
    ]
    return initialize_agent(
        tools=tools,
        llm=self._llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
        verbose=self._config.verbose)

  def run(self, question: str) -> str:
    """Answer a natural-language question with live web context."""
    cleaned = question.strip()
    if not cleaned:
      raise ValueError("Question must be a non-empty string.")
    result = self._agent.invoke({"input": cleaned})
    return result["output"]
