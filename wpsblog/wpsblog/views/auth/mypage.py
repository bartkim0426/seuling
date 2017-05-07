from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin


class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = "auth/mypage.html"

# class MyPageView(LoginRequiredMixin, View):
# 
#     def get(self, request, *args, **kwargs):
#         return render(
#                 request,
#                 "auth/mypage.html",
#                 {},
#                 )
# @login_required
# def mypage(request):
# 
#     return render(
#             request,
#             "auth/mypage.html",
#             {},
#             )
