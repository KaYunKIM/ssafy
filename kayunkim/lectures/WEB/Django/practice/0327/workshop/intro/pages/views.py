from django.shortcuts import render
# Create your views here.

def dinner(request,menu, ppl):
    context = {
        'menu':menu,
        'ppl':ppl
    }
    return render(request, 'dinner.html',context)