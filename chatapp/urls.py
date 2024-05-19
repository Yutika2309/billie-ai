from views import *
from rest_framework import routers
from django.urls import path, include

urlpatterns = [
    path('billiechat', BillieChatView.as_view(), name='chat-with-billie')
]