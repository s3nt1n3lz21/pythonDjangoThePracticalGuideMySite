from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug>", views.post_detail, name="post-detail-page"),
    re_path(r'.*', views.page404)
]
