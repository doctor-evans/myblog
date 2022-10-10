from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path("", views.welcomeView, name="welcome"),
    path("home/", views.indexView, name="home"),
    path("about-us/", views.aboutUsView, name="aboutview"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]
