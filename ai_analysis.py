import os, openai
from llama_index import SimpleDirectoryReader , GPTVectorStoreIndex
from dotenv import load_dotenv
from keys import api_key

os.environ['OPENAI_API_KEY']=api_key
load_dotenv('openai.env')
openai.api_key=os.getenv('OPENAI_API_KEY')

# Using keys for API_authentication
class Analyze (SimpleDirectoryReader,GPTVectorStoreIndex):
    
    def __init__(self,inquire,Doc='Guide'):
        
        self.Doc = SimpleDirectoryReader(Doc).load_data()
        self.index = GPTVectorStoreIndex.from_documents(self.Doc)
        self.Query = self.index.as_query_engine()
        self.response = self.Query.query(inquire)

    def respond(self):
        print (self.response)


if __name__ == '__main__':
    
    A=Analyze('Who is the author of this document?')
    A.respond()