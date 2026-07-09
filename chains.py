"""
LangChain pipeline for grammar correction.

Pipeline:
PromptTemplate
      ↓
ChatOllama (Llama 3.2)
      ↓
Structured Output (GrammarResponse)
"""
from langchain_ollama import ChatOllama

from prompts import grammar_prompt
from models import GrammarResponse
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)
structured_llm = llm.with_structured_output(
    GrammarResponse
)
grammar_chain = grammar_prompt | structured_llm