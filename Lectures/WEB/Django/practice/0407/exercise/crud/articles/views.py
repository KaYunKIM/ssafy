from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

#form 사용
def create(request):
    #1. POST 요청일 경우: 작성된 게시글이 온 경우
    if request.method == 'POST':                      #작성된 게시글 data를 form에 담기
        form = ArticleForm(request.POST)              #form에 담긴 data가 유효한지 검증하기
        if form.is_valid():                           #유효한 data인지 판별하기
            form.save()                               #valid data일 경우, database에 저장하기
            return redirect('articles:index')
    #2. GET 요청일 경우: 게시글 작성 페이지 보여주기
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)