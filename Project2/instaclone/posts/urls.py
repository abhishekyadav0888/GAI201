from django.urls import path
from .views import create_post, view_posts, delete_post

urlpatterns = [
    path('create/', create_post, name='create-post'),
    path('view/', view_posts, name='view-posts'),
    path('delete/<int:post_id>/', delete_post, name='delete-post'),
]
