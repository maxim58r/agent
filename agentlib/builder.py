from __future__ import annotations

from typing import Sequence
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent


def build_agent(tools: Sequence) -> AgentExecutor:
    """Создает и возвращает LangChain агент."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
