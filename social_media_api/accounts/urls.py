from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('follow/<int:pk>/', views.FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', views.UnfollowUserView.as_view(), name='unfollow-user'),
]