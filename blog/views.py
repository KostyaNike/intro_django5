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

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
        'published_recently': post.published_recently()
    }

    return render(
    request, 'blog/post_detail.html', 
    context=context,
    )