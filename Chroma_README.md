🤖 Customer Support FAQ Chatbot
Semantic Search Chatbot using LangChain, HuggingFace & Chroma








A lightweight Customer Support Chatbot that answers FAQ questions using semantic similarity search instead of traditional keyword matching.

It converts support documents into vector embeddings and stores them in a vector database, allowing the bot to retrieve the most relevant answer to user queries.

📌 Features

✨ Semantic search using embeddings
📚 Local vector database with persistence
⚡ Fast similarity-based retrieval
💬 Interactive CLI chatbot
🧠 Uses lightweight transformer embedding model

🏗️ Architecture
User Question
      │
      ▼
Text Embedding (HuggingFace)
      │
      ▼
Chroma Vector Database
      │
      ▼
Similarity Search
      │
      ▼
Most Relevant FAQ
      │
      ▼
Chatbot Response

Technologies used:

LangChain

Chroma

Hugging Face Transformers

Sentence-Transformers

📂 Project Structure
customer-support-chatbot
│
├── support_bot.py
├── support_db/
│
└── README.md
File	Description
support_bot.py	Main chatbot script
support_db/	Stored vector embeddings
README.md	Project documentation

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/customer-support-chatbot.git
cd customer-support-chatbot

2️⃣ Install dependencies
pip install langchain
pip install langchain-community
pip install langchain-huggingface
pip install chromadb
pip install sentence-transformers

Or install everything at once:

pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers
🚀 Running the Chatbot

Start the chatbot:

python support_bot.py

Example interaction:

Ask Customer Support: How can I track my order?

Support Bot:
You can track your order using the tracking link sent to your email.

Exit the chatbot:

exit
🧠 Knowledge Base Example

The chatbot currently uses the following FAQ dataset:

support_docs = [
"You can reset your password by clicking the 'Forgot Password' option on the login page.",
"Orders usually take 3 to 5 business days for delivery.",
"You can track your order using the tracking link sent to your email.",
"Refunds are processed within 7 business days after approval.",
"You can contact customer support via support@company.com."
]
🔎 How Similarity Search Works

1️⃣ Convert documents into embeddings
2️⃣ Store embeddings in Chroma DB
3️⃣ Convert user query into embedding
4️⃣ Search for most similar vector
5️⃣ Return the best matching document

📊 Example Queries

Try asking:

How do I reset my password?

How long does delivery take?

Where can I track my order?

How long do refunds take?

How can I contact support?



👨‍💻 Author

Muthukumar
AI / ML Enthusiast


