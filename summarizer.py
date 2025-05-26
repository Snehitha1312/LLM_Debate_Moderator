from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document

def generate_summary(history):
    llm = ChatOpenAI(temperature=0.5, model="gpt-4")
    chain = load_summarize_chain(llm, chain_type="refine")
    docs = [Document(page_content=history)]
    return chain.run(docs)
