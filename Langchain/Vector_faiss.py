# step 1 : install package 

# pip install VectorStores
# pip install langchain-community faiss-cpu

#step 2

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

#step 3

texts = [
    "LangChain helps build LLM applications",
    "FAISS is used for vector similarity search",
    "this is my first AI course"
]

#step 4

embeddings_new = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  #embedding model copied from huggingface site

#step 5

vectorstore1 = FAISS.from_texts(texts,embeddings_new)

#step 6

vectorstore1.save_local("my vector file")  # file saved in local folder