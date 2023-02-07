from django.urls import path
from knox import views as knox_views

from .views import RegisterAPI,LoginAPI,StudentProfile

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/student/edit/<int:pk>', StudentProfile.as_view(),name='student'),
]