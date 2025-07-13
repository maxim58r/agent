"""Точка входа для запуска агента через CLI или API."""

from __future__ import annotations

import argparse

from agentlib.builder import build_agent
from agentlib.tools import get_default_tools
from agentlib.cli import run_cli
from agentlib.api import create_app


def main() -> None:
    parser = argparse.ArgumentParser(description="Universal LangChain Agent")
    parser.add_argument("--api", action="store_true", help="Запустить HTTP API вместо CLI")
    args = parser.parse_args()

    tools = get_default_tools()
    agent = build_agent(tools)

    if args.api:
        import uvicorn

        app = create_app(agent)
        uvicorn.run(app, host="127.0.0.1", port=8000)
    else:
        run_cli(agent)


if __name__ == "__main__":
    main()
