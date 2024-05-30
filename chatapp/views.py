from rest_framework import generics
from .models import ClassDetails
from .serializers import ClassDetailsSerializer

class ClassDetailsListCreateView(generics.ListCreateAPIView):
    queryset = ClassDetails.objects.all()
    serializer_class = ClassDetailsSerializer

class ClassDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassDetails.objects.all()
    serializer_class = ClassDetailsSerializer
