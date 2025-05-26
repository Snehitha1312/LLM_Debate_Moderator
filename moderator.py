from langchain_openai import ChatOpenAI
from prompts import MODERATOR_PROMPT

llm = ChatOpenAI(temperature=0.7, model="gpt-4")

def moderator_intervene(topic, history):
    return llm(MODERATOR_PROMPT.format(topic=topic, history=history)).content
