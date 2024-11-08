from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre

# Create your views here.
@require_safe
def index(request):
    '''
    전체 영화 목록 페이지 조회
    '''
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    '''
    필터링된 영화 데이터 제공
    '''
    
    pass


@require_safe
def recommended(request):
    pass
