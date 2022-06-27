from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Quotes, Links
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "post_detail.html"


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


def quote_view(request):
    template_name = "base.html"
    all_quotes = Quotes.objects.all()

    return render(request, "base.html", {"all_quotes": all_quotes})


def sociallinks(request):
    links = Links.objects.all().first()
    return render(request, "footer.html", {"links": links})
