from rest_framework import generics, permissions
from .models import CustomUser  # Import your custom user model
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to register

@csrf_exempt
def handle_options_register(request):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response['Access-Control-Max-Age'] = '86400'
    return response