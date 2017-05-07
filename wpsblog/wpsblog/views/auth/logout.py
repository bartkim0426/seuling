from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import View


class LogoutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)

        return render(
                request,
                "posts/list.html",
                {},
                )
# def logout(request):
# 
#     auth_logout(request)
# 
#     return render(
#             request,
#             "posts/list.html",
#             {},
#             )
