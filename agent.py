"""
Business logic for AI agent with knowledge base integration.
"""
from dotenv import load_dotenv
load_dotenv()
import os
from llama_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.llms import ChatMessage, MessageRole

retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id=os.getenv("BEDROCK_KNOWLEDGE_BASE_ID"),
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 3}},
    )
llm = OpenAI(model=os.getenv("OPENAI_MODEL"))

_knowledge_base_tool = QueryEngineTool.from_defaults(
    query_engine=RetrieverQueryEngine(retriever=retriever),
    name="amazon_knowledge_base",
    description=(
        "A vector database of knowledge about companies and their financial data."
    ),
)

agent = ReActAgent(
    tools=[_knowledge_base_tool],
    llm=llm,
    system_prompt=(
        "You are a helpful AI assistant with access to a vector database of knowledge about companies and their financial data. "
        "When users ask questions about companies or their financial data, "
        "use the available tool to retrieve accurate information. "
        "Always provide clear and concise answers based on the retrieved information."
        "You must use English language for your responses and provide the answer in a concise manner."
    ),
)


async def get_agent_response(message, chat_history):
    messages = []
    for msg in chat_history:
        if msg["role"] == "user":
            messages.append(ChatMessage(role=MessageRole.USER, content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=msg["content"]))
    
    user_message = ChatMessage(role=MessageRole.USER, content=message)
    
    response = await agent.run(user_message, chat_history=messages)
    return str(response)