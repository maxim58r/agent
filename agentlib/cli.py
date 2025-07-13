from __future__ import annotations

from langchain.agents import AgentExecutor


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
