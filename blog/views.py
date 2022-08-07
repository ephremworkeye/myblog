from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all() # select * from Post
    return render(request, 'blog/blog_post.html', {'posts': posts})

def post_detail(request):
    post = Post.objects.get(id=2)
    return render(request, 'blog/post_detail.html', {'post':post})