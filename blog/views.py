from django.shortcuts import render
from blog.models import Post

# Create your views here.

def Posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }

    return render(
        request,
        'blog/post.html',
        context=context,
    )