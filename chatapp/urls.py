from django.urls import path
from .views import DocumentChatView, ChatDetailsDetailView

urlpatterns = [
    path('chat-details/', DocumentChatView.as_view(), name='class-details-list-create'),
    path('chat-details/<int:pk>/', ChatDetailsDetailView.as_view(), name='class-details-detail')
]
