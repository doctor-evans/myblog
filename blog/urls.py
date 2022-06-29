from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path("", views.indexView, name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("base/links/", views.sociallinks, name="links"),
]
