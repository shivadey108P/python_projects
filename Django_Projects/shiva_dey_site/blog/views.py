from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post

all_posts = Post.objects.all().order_by("-date")

# Create your views here.


def index(request):
    latest_posts = all_posts[:3]
    return render(
        request, "blog/index.html", {"year": date.today().year, "posts": latest_posts}
    )


def all_posts_view(request):
    return render(request, "blog/all_posts.html", {"posts": all_posts})


def post_details(request, slug):
    # requested_post = next(post for post in all_posts if slug in post.slug)
    requested_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post_details.html",
        {"post": requested_post, "post_tags": requested_post.tag.all()},
    )
