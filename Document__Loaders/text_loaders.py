from langchain_community.document_loaders import TextLoader


file_path = "data/1.txt"

loader = TextLoader(file_path)
documents = loader.load()

print(type(documents))
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)
