from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from llmutils.processor import *

# Create your views here.
class BillieChatView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            query = self.request.data.get('query', None)

            if query:
                document_chat = BillieChat()  
                response = document_chat.chat(query)
                return Response(response.response)
            else:
                return Response({'error': 'Query parameter is required'}, status=400)
        except Exception as e:
            print("EXCEPTION:", e)
            return Response({'error': 'An error occurred. Please try again later.'}, status=400)