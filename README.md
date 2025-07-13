# Universal LangChain Agent

Этот проект демонстрирует работу простого агента на базе LangChain.
Агент расширяем и предоставляет CLI и HTTP API.

## Требования

- Python 3.11+
- Переменная окружения `OPENAI_API_KEY` для доступа к ChatOpenAI

Установите зависимости:

```bash
pip install langchain langchain-openai langchain-community \
    langchain-experimental requests fastapi uvicorn
```

## Запуск CLI

```bash
python universal_agent.py
```

Для выхода введите `exit` или `quit`.

## Запуск API

```bash
python universal_agent.py --api
```

HTTP сервер будет запущен на `http://127.0.0.1:8000`. POST запрос на `/chat`
принимает JSON вида `{"input": "ваш вопрос"}` и возвращает ответ агента.

## Встроенные инструменты

- **Калькулятор** для математических выражений
- **Приветствие** (пример пользовательской функции)
- **REST API**: GET‑запрос по URL
- **Чтение файлов** из локальной файловой системы
- **Python REPL** для выполнения кода

## Расширение

Добавляйте свои инструменты в модуле `agentlib/tools.py` и
подключайте их при сборке агента.
