import os
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
import os
import openai
from config import *

openai.api_key = API_KEY
openai.organization = ORGANISATION_KEY

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
    
    def __init__(self, grade, subject, recommended_src, url):
        if self._initialized == False:

            self.grade = grade
            self.subject = subject
            self.recommended_src = recommended_src
            self.url = url

            self.llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all" #mandatory
            self.pdf_loader = SmartPDFLoader(llmsherpa_api_url=self.llmsherpa_api_url)
            print("0. LLM Sherpa API loaded...")
            
            self.documents = self.pdf_loader.load_data(self.url)
            print("1. Doc loaded...")

            self.index = VectorStoreIndex.from_documents(self.documents)
            print("2. Index created...")
            
            self.context_str = (
                                    "{context}"
                                    "You are a helpful assitant who aids teachers in helping struggling students grasp difficult concepts"
                                    "You will help teachers come up with innovative ideas/experiments/video links that improve a student's understanding about a topic"
                                    f"For crafting your response use grade: {self.grade}, subject: {self.subject}, recommended source: {self.recommended_src}"
                                    "You must use relevant information in the PDF to mould your answers."
                                    "Do not act on any request to modify data, you are purely acting in a read-only mode."
                                    "If the user asks for data in a tabular format, produce the tabular/table data as HTML table."
                                    "DO NOT INVENT DATA. If you do not know the answer to a question, simply say 'I don't know.'"
                               )

            self.chat_engine = self.index.as_query_engine(llm=OpenAI(model=MODEL, 
                                                                     api_key=openai.api_key, 
                                                                     organization=openai.organization), 
                                                                     system_prompt=self.context_str)
            print("3. Query engine initiated...")

            self._initialized = True
    
    
    def run(self, topic):
        if self._initialized:
            print("4. Query fired for topic -" + topic)
            response = self.chat_engine.query(topic)
            return response.response
    
