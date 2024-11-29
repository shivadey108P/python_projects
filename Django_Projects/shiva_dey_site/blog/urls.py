from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/posts', views.all_posts_view, name='all-posts'),
    path("/posts/<slug:slug>", views.post_details, name="post-detail-page")
]
