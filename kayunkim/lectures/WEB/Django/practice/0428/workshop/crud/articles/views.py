from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user in article.like_users.all():
    # if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
