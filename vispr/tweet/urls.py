
from django.urls import path

from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('tweet_edit/<int:tweet_id>', views.tweet_edit, name='tweet_edit'),
    path('tweet_delete/<int:tweet_id>', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
]
