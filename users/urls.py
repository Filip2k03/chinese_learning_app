from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('profile/', views.UserDetailView.as_view(), name='user-profile'),  
    path('buy-premium/', views.BuyPremiumView.as_view(), name='buy-premium'), # Add this
]