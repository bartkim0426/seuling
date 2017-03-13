from django.template import loader
from django.shortcuts import render


def room(request, room_id):
   # 방 번호 (room_id) 직방의 데이터를 그대로 보여주는 뷰 (컨트롤러)
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
            response.content,
            content_type="application/json",
            )

