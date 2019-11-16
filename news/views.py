from django.shortcuts import HttpResponse, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, TemplateView
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
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', published__year=year,
                             published__month=month, published__day=day)
    return render(request, 'news/post/detail.html', {'post': post})


def author(request):
    return render(request, 'news/author.html')
