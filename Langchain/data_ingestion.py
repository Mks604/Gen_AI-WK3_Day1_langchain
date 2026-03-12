# pip install langchain_community

# pip install bs4 - for webpage URL

# pip install arxiv

# pip install pymupdf

# pip install wikipedia


from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import ArxivLoader
from langchain_community.document_loaders import WikipediaLoader


#1 - text file

test = TextLoader("notes.txt")

test.load()

# Output : 
# [Document(metadata={'source': 'notes.txt'}, page_content='"This is the Gen AI couese method lession "')]


# 2 - Web URL 

test2 = WebBaseLoader(web_path="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/")

test2.load() 



# 3 - Research paper ex


test3 = ArxivLoader(query="1706.03762")  # web URL page ID https://arxiv.org/abs/1706.03762

test3.load()

#output : [Document(metadata={'Published': '2023-08-02', 'Title': 'Attention Is All You Need', 'Authors': 'Ashish Vaswani, Noam Shazeer


# 4 -  wikipedia

test4 = WikipediaLoader(query="AI agents", load_max_docs=2)

test4.load()


