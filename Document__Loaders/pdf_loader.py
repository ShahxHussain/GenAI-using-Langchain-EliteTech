from langchain_community.document_loaders import PyPDFLoader


file_path = "data/autofix.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

# print(type(docs))  
# print(len(docs))
# print(docs[3].page_content)
print(docs[0].metadata)
