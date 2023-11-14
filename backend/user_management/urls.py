from django.urls import path
from . import views
from .views import register_user
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('user_management/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('user_management/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
