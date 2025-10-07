from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
# import os

# books_dir = os.path.join(os.path.dirname(__file__), 'books')
loader = DirectoryLoader(
    path = "data",
    glob = '*.pdf,*.txt',
    loader_cls = PyPDFLoader, TextLoader
)

docs = list(docs)
docs = loader.load()
print(len(docs))













# docs = loader.lazy_load()
# for documents in docs:
#     print(docs[2].page_content)