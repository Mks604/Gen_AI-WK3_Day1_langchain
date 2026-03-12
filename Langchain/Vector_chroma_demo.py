# imports
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# sample customer support FAQ
support_docs = [
    "You can reset your password by clicking the 'Forgot Password' option on the login page.",
    "Orders usually take 3 to 5 business days for delivery.",
    "You can track your order using the tracking link sent to your email.",
    "Refunds are processed within 7 business days after approval.",
    "You can contact customer support via support@company.com."
]

# create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# create Chroma vector database
vector_db = Chroma.from_texts(
    support_docs,
    embedding=embedding_model,
    persist_directory="support_db"
)

# save database
vector_db.persist()

print("Customer support database created!")

# chatbot loop
while True:

    query = input("\nAsk Customer Support (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    results = vector_db.similarity_search(query, k=1)

    print("\nSupport Bot:")
    print(results[0].page_content)