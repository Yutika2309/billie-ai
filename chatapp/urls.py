from django.urls import path
from .views import ClassDetailsListCreateView, ClassDetailsDetailView

urlpatterns = [
    path('class-details/', ClassDetailsListCreateView.as_view(), name='class-details-list-create'),
    path('class-details/<int:pk>/', ClassDetailsDetailView.as_view(), name='class-details-detail')
]
