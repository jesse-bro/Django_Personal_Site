from django.conf.urls import url
from django.urls import path
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    path('', ListView.as_view(
        queryset=Post.objects.all().order_by("-pub_date")[:25],
        template_name="blog/blog.html",
    )),

    path('<int:pk>/', DetailView.as_view(
        model=Post,
        template_name="blog/post.html",
    ), name="post"),

    path('<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
]
