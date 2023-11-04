from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import Chroma
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings
)

documents = database.similarity_search("飛行車の最高速度は？")
print(f"ドキュメントの数： {len(documents)}")

for document in documents:
    print(f"ドキュメントの内容： {document.page_content}")
