from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'articles/ping.html')

def pong(request):
    message = request.GET.get('message')
    #template 변수
    context = {
        'message' : message,
    }
    return render(request, 'articles/pong.html', context)