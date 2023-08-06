from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    return render(request, 'articles/create.html')



