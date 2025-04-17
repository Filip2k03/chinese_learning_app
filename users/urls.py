from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('register/', views.handle_options_register, name='register_options'),
]