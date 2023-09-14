from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post

def get_date(post):
    return post['date']

def starting_page(request):
    lastest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": lastest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    this_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": this_post,
        "post_tags": this_post.tags.all()
    })

def page404(Request):
    raise Http404()