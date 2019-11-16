from django.shortcuts import HttpResponse, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, TemplateView

from news.forms import EmailForm, CommentForm
from .models import Post


# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'news/post/list.html'


class HomePage(TemplateView):
    template_name = 'home.html'


def home_page(request):
    return render(request, 'home.html')


def post_list(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/post/list.html', {'page': page, 'posts': posts})


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = EmailForm()
    return render(request, 'news/send_email.html', {'form': form})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', published__year=year,
                             published__month=month, published__day=day)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, 'news/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'form': form})


def author(request):
    return render(request, 'news/author.html')
