from __future__ import annotations

import requests
from langchain.tools import tool
from langchain_experimental.tools.python.tool import PythonREPLTool


@tool
def calculate(expression: str) -> str:
    """Вычисляет математическое выражение."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as exc:
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
    except Exception as exc:
        return f"Ошибка API: {exc}"


@tool
def read_file(path: str) -> str:
    """Читает файл и возвращает его содержимое."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as exc:
        return f"Ошибка чтения файла: {exc}"


def get_default_tools():
    """Возвращает список инструментов по умолчанию."""
    python_repl = PythonREPLTool()
    return [calculate, greet, call_api, read_file, python_repl]
