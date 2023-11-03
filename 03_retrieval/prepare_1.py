from langchain.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

print(f"ドキュメントの数： {len(documents)}")
print(f"1つめのドキュメントの内容： {documents[0].page_content}")
print(f"1つめのドキュメントのメタデータ： {documents[0].metadata}")
