from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'community/index.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'community/movie_detail.html', context)

def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'movie': movie,
        'review': review,
        'form': form,
    }
    return render(request, 'community/review_detail.html', context)

@login_required
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('community:movie_detail', movie_pk )
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request, 'community/review_form.html', context)

@login_required
def review_edit(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method=="POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('community:review_detail', movie_pk, review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'community/review_form.html', context)

@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == review.user:
        review.delete()
    return redirect('community:movie_detail', movie_pk)

@require_POST
def comment_create(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
        return redirect('community:review_detail', movie_pk, review_pk)
    else:
        return redirect('accounts:login')

def comment_edit(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = CommentForm(instance=review)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
        return redirect('community:review_detail', movie_pk, review_pk)
    else:
        return redirect('accounts:login')

@login_required
def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('community:review_detail', movie_pk, review_pk)

def like(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('community:review_detail', movie_pk, review_pk)
