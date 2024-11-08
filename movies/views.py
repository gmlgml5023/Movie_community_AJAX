from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse

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
    genre_name = request.GET.get('genre', '')
    # 장르가 선택되었으면
    if genre_name:
        movies = Movie.objects.filter(genres__name=genre_name).values('title')
    else:
        movies = Movie.objects.all().values('title')

    movies_list = list(movies)  # QuerySet을 list로 변환하여 반환

    return JsonResponse(movies_list, safe=False)


@require_safe
def recommended(request):
    pass
