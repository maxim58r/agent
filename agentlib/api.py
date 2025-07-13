from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.agents import AgentExecutor


class Query(BaseModel):
    input: str


def create_app(agent: AgentExecutor) -> FastAPI:
    """Создает FastAPI приложение для взаимодействия с агентом."""
    app = FastAPI()

    @app.post("/chat")
    async def chat(query: Query):
        try:
            result = agent.invoke({"input": query.input})
            return {"output": result["output"]}
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    return app
