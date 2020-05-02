from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

@login_required
def review_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('community:review_detail', review.pk)
        else:
            form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'community/review_create.html', context)
    else:
        return redirect('accounts:login')

def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'review': review,
        'form': form
    }
    return render(request, 'community/review_detail.html', context)

@login_required
def review_update(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user == request.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    form.save()
                    return redirect('community:review_detail', review.pk)
            else:
                form = ReviewForm(instance=review)
            context = {
                'form': form
            }
            return render(request, 'community/review_update.html', context)
        else:
            return redirect('community:review_detail', review.pk)
    else:
         return redirect('accounts:login')

@require_POST
@login_required
def review_delete(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user == request.user:
            review.delete()
            return redirect('community:index')
        else:
            return redirect('community:review_detail', review.pk)
    else:
        return redirect('accounts:login')

@login_required
def comment_create(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.review = review
                comment.save()
        return redirect('community:review_detail', review.pk)
    else:
        return redirect('accounts:login')
    '''
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'community/comment_create.html', context)
    '''

@login_required
def comment_delete(request, review_pk, comment_pk):
    if request.user.is_authenticated():
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
        return redirect('community:review_detail', review_pk)
    else:
        return redirect('accounts:login')