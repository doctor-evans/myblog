from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Quotes, Links, AboutUs
from .forms import CommentForm


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "post_detail.html"


def indexView(request):
    template_name = "index.html"
    all_quotes = Quotes.objects.all()
    post_list = Post.objects.filter(status=1).order_by("-created_on")
    links = Links.objects.all().first()

    return render(
        request,
        "index.html",
        {"all_quotes": all_quotes, "post_list": post_list, "links": links},
    )


def post_detail(request, slug):
    template_name = "post_detail.html"
    all_post = Post.objects.all()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "all_post": all_post,
            "comments": comments,
            "new_comments": new_comment,
            "comment_form": comment_form,
        },
    )


def aboutUsView(request):
    about = AboutUs.objects.all().first()
    return render(request, "about.html", {"about": about})
