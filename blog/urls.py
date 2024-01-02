from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('post/', views.post, name='blog-post'),
    path('categories/', views.categories, name='blog-category'),
]