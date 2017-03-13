#from django.shortcuts import render

#
#def about(request):
#    return render(
#            request, 
#            "about.html",
#            )

# 1. 가장 먼저 HttpResponse
# from django.http import HttpResponse
#
#def about(request):
#    return HttpResponse("about")

# 2. loader로 사용
#
#from django.template import loader
#from django.http import HttpResponse
#
#def about(request):
#    # 1. template 객체 생성
#    template = loader.get_template("about.html")
#    # 2. HttpResponse로 template.render를 받음
#    # render가 뭐를 받는지? 알고 싶으면 embed를 걸고
#    # template.render? 물어보면 됨: context, request를 받는다
#    return HttpResponse(
#            template.render(
#                {} , 
#               request, 
#                )
#            ) # 이러면 about.html을 뿌려준다.

# 3. 이걸 한번에 해주는 shortcuts의 render 사용
# render 함수는 (request, template_name, context) 세가지를 받음
# 위의 loader, HttpResponse를 축약 시켜준 것! 
from django.shortcuts import render

def about(request):
    return render(
           request,
           "about.html",
           {},
            )
