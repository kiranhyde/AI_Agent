"""CLI entry point for the LangChain web-search agent."""

from __future__ import annotations

import argparse
import sys

from ai_agent import AgentConfig, WebSearchAgent


def parse_args() -> argparse.Namespace:
  """Return parsed CLI arguments."""
  parser = argparse.ArgumentParser(
      description="Ask the agent any web-searchable question.")
  parser.add_argument(
      "question",
      nargs="?",
      help="Question to send to the agent. Reads from stdin if omitted.")
  parser.add_argument(
      "-m",
      "--model",
      default="gpt-4o-mini",
      help="OpenAI model identifier to use.")
  parser.add_argument(
      "-t",
      "--temperature",
      type=float,
      default=0.1,
      help="Sampling temperature for the LLM.")
  parser.add_argument(
      "-r",
      "--max-results",
      type=int,
      default=4,
      help="Maximum number of Tavily search results.")
  parser.add_argument(
      "-v",
      "--verbose",
      action="store_true",
      help="Enable LangChain debug logging.")
  return parser.parse_args()


def main() -> int:
  """Entrypoint used by the CLI."""
  args = parse_args()
  question = args.question or input("Enter your question: ").strip()
  config = AgentConfig(
      model=args.model,
      temperature=args.temperature,
      max_search_results=args.max_results,
      verbose=args.verbose)
  agent = WebSearchAgent(config=config)
  try:
    answer = agent.run(question)
  except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    return 1
  print(answer)
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
