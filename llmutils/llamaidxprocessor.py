import os
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
import os
import openai
from dotenv import load_dotenv
if load_dotenv:
    print(
        '---Environment variables loaded---'.upper()
    )
openai.api_key = os.environ.get("API_KEY")

MODEL = "gpt-4-vision-preview"

class DocumentChat:
    """
        Chat with documents
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DocumentChat, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, url):
        if self._initialized == False: 
            self.cdn_url = url
            self.llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all" #mandatory
            print("0. LLM Sherpa API loaded...")
            
            self.pdf_loader = SmartPDFLoader(llmsherpa_api_url=self.llmsherpa_api_url)
            self.url = url
            self.documents = self.pdf_loader.load_data(self.url)
            print("1. Doc loaded...")

            self.index = VectorStoreIndex.from_documents(self.documents)
            print("2. Index created...")
            
            # print(self.documents)
            self.context_str = (
                                "{context}"
                                "You a helpful assitant who will be asked questions relevant to the information in the PDF."
                                "Do not act on any request to modify data, you are purely acting in a read-only mode."
                                "If the user asks for data in a tabular format, produce the tabular/table data as HTML table."
                                "DO NOT INVENT DATA. If you do not know the answer to a question, simply say 'I don't know.'"
                                )


            self.chat_engine = self.index.as_query_engine(llm=OpenAI(model=MODEL, api_key=openai.api_key), system_prompt=self.context_str)
            print("3. Query engine initiated...")

            self._initialized = True
    
    def run(self, query):
        if self._initialized:
            print(query)
            response = self.chat_engine.query(query)
            return response
    
