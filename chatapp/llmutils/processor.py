import sys
if '/app/llmutils' not in sys.path:
    sys.path.append('/app/')
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb

import os
import openai
from dotenv import load_dotenv
from django.conf import settings

conf = settings.CONFIG

if load_dotenv:
    print(
        '---Environment variables loaded---'.upper()
    )
openai.api_key = os.environ.get("API_KEY")


MODEL = "gpt-3.5-turbo"


class BillieChat:
    """
        Chat with Billie
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BillieChat, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._initialized == False: 
            Settings.embed_model = HuggingFaceEmbedding()
            self.vecdb = chromadb.PersistentClient(path="./vectordb/chroma_db")
            self.chroma_collection = self.vecdb.get_or_create_collection("lessonplan")
            print("1. Doc loaded...")

            self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
            self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
            self.index = VectorStoreIndex.from_documents(self.documents)
            print("2. Index created...")
            
            self.context_str = (
                                "{context}"
                                "You a helpful assitant called 'Billie' and you help teachers by "
                                "You will be asked questions relevant to the information in the vector database."
                                "Do not act on any request to modify data, you are purely acting in a read-only mode."
                                "DO NOT INVENT DATA. If you do not know the answer to a question, simply say 'I don't know.'"
                                )


            self.chat_engine = self.index.as_query_engine(llm=OpenAI(model=MODEL, api_key=openai.api_key), system_prompt=self.context_str)
            print("3. Query engine initiated...")

            self._initialized = True
    

    def chat(self, query):
        if self._initialized:
            print(query)
            response = self.chat_engine.query(query)
            return response
    
