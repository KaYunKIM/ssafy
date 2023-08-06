from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies': movies,
        'page_obj': page_obj,
    }
    return render(request, 'movies/index.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    base_url = 'https://image.tmdb.org/t/p'
    poster_url = movie.poster_path
    image_url = base_url + '/w500' + poster_url
    #https://image.tmdb.org/t/p/<image_size>/<poster_path> 의 URL
    # print(movie.genres_set.all())
    context = {
        'movie': movie,
        'image_url': image_url,
    }
    return render(request, 'movies/movie_detail.html', context)

def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'movie': movie,
        'review': review,
        'form': form,
    }
    return render(request, 'movies/review_detail.html', context)

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
            return redirect('movies:movie_detail', movie_pk )
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/review_form.html', context)

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
            return redirect('movies:review_detail', movie_pk, review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/review_form.html', context)

@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:movie_detail', movie_pk)

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
        return redirect('movies:review_detail', movie_pk, review_pk)
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
        return redirect('movies:review_detail', movie_pk, review_pk)
    else:
        return redirect('accounts:login')

@login_required
def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:review_detail', movie_pk, review_pk)

def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(id=request.user.pk).exists():
        movie.like_users.remove(request.user)
        liked = False
    else:
        movie.like_users.add(request.user)
        liked = True

    data = {
        'liked' : liked,
        'count' : movie.like_users.count()
    }
    return JsonResponse(data)


def recommended(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    users = movie.like_users.filter(id=request.user.pk)
    context = {
        'users': users
    }
    return render(request, 'movies/recommended.html', context)

@login_required
def recommend(request):
    movies = Movie.objects.all()
    like_movies = request.user.like_movies.all()
    like_genres = {}
    for movie in like_movies:
        print(f'123 {movie}')
        for genres in movie.genres.all():
            print(f'333 {genres}')
            if genres.name in like_genres.keys():
                like_genres[genres.name] += 1
            else:
                like_genres[genres.name] = 1
    most_liked_genres = like_genres
    recommend_movies = Movie.objects.all().order_by('-popularity')[0:10]
    print(recommend_movies)
    context = {
        'like_genres': like_genres,
    }

    return render(request, 'movies/rec.html', context)