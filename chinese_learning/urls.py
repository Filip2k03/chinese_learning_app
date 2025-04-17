# chinese_learning/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vocabulary/', views.VocabularyListView.as_view(), name='vocabulary-list'),
    path('vocabulary/<int:pk>/', views.VocabularyDetailView.as_view(), name='vocabulary-detail'),
    path('segment/', views.segment_chinese_text, name='segment-chinese-text'), # New endpoint
]