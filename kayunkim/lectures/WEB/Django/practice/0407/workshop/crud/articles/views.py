from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

#form 사용
def create(request):
    #1. POST 요청일 경우: 작성된 게시글이 온 경우
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    #2. GET 요청일 경우: 게시글 작성 페이지 보여주기
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request,pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html' , context)

@require_POST
def delete(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request,pk):
    article=get_object_or_404(Article, pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context = {
        'form':form,
    }
    return render(request,'articles/update.html' , context)