from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    # 1. form에 담긴 값을 가져온다.
    search = request.GET.get("search")

    # 2. unsplash API 요청보내기
    CLIENT_ID = 'NwLa8u1goObqzJLk8K4s72fITpJz44KvGasQXA_5K4o'
    base_url = 'http://api.unsplash.com/'
    request_url = base_url + 'search/photos' + f'?client_id={CLIENT_ID}&query={search}'
    response = requests.get(request_url).json() #응답값을 json으로 바꿔주기

    photo_list = []
    for photo in response.get('results'):
        photo_list.append(photo.get('urls').get('regular'))

    context = {
        'photo_list': photo_list,
    }

    return render(request, 'gallery.html', context)