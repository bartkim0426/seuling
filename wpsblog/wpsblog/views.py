from django.http.response import HttpResponse  
import requests 
import json

def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
   # 방 번호 (room_id) 직방의 데이터를 그대로 보여주는 뷰 (컨트롤러) 
    response = requests.get("https://api.zigbang.com/v3/items?detail=true&item_ids=[7605634,7482966,7384843,7538229,7572997,7672923,7681182,7657670,7412786,7648907,7665249,7638109,7659804,7648237,7667831,7652329,7683534,7646294,7536759,7641218,7672951,7627889,7541148,7681346,7557344,7581723,7685156,7585759,7681133,7683001,7671901,7680157,7673739,7549589,7680117,7631472,7275856,7359571,7681521,7685889,7558452,7681432,7660070,7564102,7683330,7579698,7606940,7658551,7493987,7385521,7214200,7037554,7264875,7640279,7678423,7637556,7616333,7537571,7685488,7221322]")
    data = json.loads(response.text)
    room_list = data['items']
    room_id_li = []
    for room in room_list:
        room_id_li.append(room['item']['id'])
        room_id_li.append(",")
    return HttpResponse(room_id_li)

