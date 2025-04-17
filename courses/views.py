from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer

class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_premium:
            return Course.objects.all()
        return Course.objects.filter(is_premium=False)

class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
