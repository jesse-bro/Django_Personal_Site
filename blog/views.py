from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post',pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment_to_post.html', {'form':form})