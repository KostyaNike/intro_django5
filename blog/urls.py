from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path("", blog_views.Posts, name="posts"),
    path("<int:pk>", blog_views.post_detail, name="post-detail")
]