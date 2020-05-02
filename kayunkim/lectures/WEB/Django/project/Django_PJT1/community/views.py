from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

def new_review(request):
    return render(request, 'community/new_review.html')

def create_review(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    rank = request.GET.get('rank')
    review = Review()
    review.title = title
    review.content = content
    review.rank = rank
    review.save()
    return redirect('/community/')