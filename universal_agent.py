"""Universal LangChain agent example.

Запуск: `python universal_agent.py`

Требуется Python 3.11+. Перед использованием убедитесь, что
установлены зависимости:

```
pip install langchain langchain-openai langchain-community duckduckgo-search \
    langchain-experimental requests
```

"""

from __future__ import annotations

import os
from typing import List

import requests

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.tools.python.tool import PythonREPLTool


@tool
def calculate(expression: str) -> str:
    """Вычисляет математическое выражение."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as exc:  # minimal обработка ошибок
        return f"Ошибка вычисления: {exc}"


@tool
def greet(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    return f"Привет, {name}!"


@tool
def call_api(url: str) -> str:
    """Отправляет GET-запрос по указанному URL."""
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text[:1000]
    except Exception as exc:  # минимальная обработка ошибок
        return f"Ошибка API: {exc}"


@tool
def read_file(path: str) -> str:
    """Читает файл и возвращает его содержимое."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as exc:
        return f"Ошибка чтения файла: {exc}"


def build_agent(tools: List) -> AgentExecutor:
    """Создает и возвращает LangChain агент с заданными инструментами."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = create_react_agent(llm, tools)
    return AgentExecutor(agent=prompt, tools=tools, verbose=True)


def run_cli(agent: AgentExecutor) -> None:
    """Запускает простой CLI для общения с агентом."""
    print("Введите запрос (или 'exit' для выхода):")
    while True:
        user_input = input(" > ")
        if user_input.lower() in {"exit", "quit"}:
            break
        try:
            response = agent.invoke({"input": user_input})
            print(response["output"])
        except Exception as exc:
            print(f"Ошибка при обработке запроса: {exc}")


if __name__ == "__main__":
    # Регистрируем инструменты
    search_tool = DuckDuckGoSearchRun()
    python_repl = PythonREPLTool()
    tools = [
        search_tool,
        calculate,
        greet,
        call_api,
        read_file,
        python_repl,
    ]

    agent = build_agent(tools)
    run_cli(agent)
