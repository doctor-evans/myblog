from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    # meta description is for search engines like google
    meta_description = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="images", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class Links(models.Model):
    twitter = models.URLField(null=True, blank=True, default='')
    facebook = models.URLField(null=True, blank=True, default='')
    youtube = models.URLField(null=True, blank=True, default='')
    instagram = models.URLField(null=True, blank=True, default='')
    linkedin = models.URLField(null=True, blank=True, default='')


class Quotes(models.Model):
    quote = models.CharField(max_length=250)
