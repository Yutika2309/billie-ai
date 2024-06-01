from rest_framework import generics
from .models import ClassDetails
from .serializers import ClassDetailsSerializer
from rest_framework.response import Response
from llmutils.llamaidxprocessor import DocumentChat

class DocumentChatView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        grade = request.data.get('grade')
        subject = request.data.get('subject')
        recommended_src = request.data.get('recommended_src')
        topic = request.data.get('topic')
        
        try:
            class_detail = ClassDetails.objects.get(grade=grade, subject=subject, recommended_src=recommended_src, topic=topic)
        except ClassDetails.DoesNotExist:
            return Response({'error': 'ClassDetails not found.'}, status=404)
        
        document_chat = DocumentChat(grade, subject, recommended_src, class_detail.subject_url)
        response = document_chat.run(topic)
        
        return Response({'response': response})

class ChatDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassDetails.objects.all()
    serializer_class = ClassDetailsSerializer
