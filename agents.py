from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(temperature=0.7, model="gpt-4")

ENGINEER_PROMPT = """
You are an experienced software engineer. Debate the topic: "{topic}".
Your past arguments: {history}
Respond thoughtfully in 3-4 sentences from an engineering perspective.
"""

DESIGNER_PROMPT = """
You are a creative and pragmatic product designer. Debate the topic: "{topic}".
Your past arguments: {history}
Respond thoughtfully in 3-4 sentences from a design and UX perspective.
"""

PM_PROMPT = """
You are a strategic product manager. Debate the topic: "{topic}".
Your past arguments: {history}
Respond thoughtfully in 3-4 sentences from a business and timeline perspective.
"""

def engineer_response(topic, history):
    return llm.invoke(ENGINEER_PROMPT.format(topic=topic, history=history)).content

def designer_response(topic, history):
    return llm.invoke(DESIGNER_PROMPT.format(topic=topic, history=history)).content

def pm_response(topic, history):
    return llm.invoke(PM_PROMPT.format(topic=topic, history=history)).content
