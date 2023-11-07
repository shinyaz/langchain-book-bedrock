from langchain.chains import RetrievalQA
from langchain.chat_models import BedrockChat
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import Chroma
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

chat = BedrockChat(
    model_id="anthropic.claude-v2"
)

embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings
)

retriever = database.as_retriever()

qa = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True
)

result = qa("飛行車の最高速度を教えて")

print(result["result"])

print(result["source_documents"])
