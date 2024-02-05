# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView
# By using the period .views we reference the current directory, which is our pages app containing both views.py and urls.py

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
]