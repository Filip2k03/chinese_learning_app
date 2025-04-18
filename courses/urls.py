from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('lessons/<int:pk>/', views.LessonDetail.as_view(), name='lesson-detail'), # New route for lesson detail
]