from rest_framework import serializers
from .models import ClassDetails

class ClassDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetails
        fields = ['grade', 'subject', 'query_text', 'chat_response']

