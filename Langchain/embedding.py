# pip install langchain openai sentence-transformers

# pip install langchain-openai

# pip install langchain-huggingface

from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


openai_embed = OpenAIEmbeddings(openai_api_key="sk-proj-")  # with API Key OpenAI module


textemds = "this is the my AI course"

embeded = openai_embed.embed_query(textemds)
print (embeded[:4])  

# Output : [-0.014164912514388561, -0.017547370865941048, -0.011859317310154438, -0.008904842659831047]


# Huggking Face without API key 


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

textforemd = "this is the my AI course"

huggingface3 = embeddings.embed_query(textforemd)
print(huggingface3[:4])

# Output 
# [0.008572288788855076, -0.013569590635597706, -0.02405569702386856, -0.0001793685951270163]