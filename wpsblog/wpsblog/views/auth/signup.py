from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse 


class SignupView(View):
    
    def get(self, request, *args, **kwargs):
        return render(
               request,
               "auth/signup.html",
               {},
               )
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                )

        return redirect(
               reverse(
                   "auth:login" 
                  ) 
                )


# def signup(request):
#     if (request.method == "POST"):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         email = request.POST.get("email")
# 
#         user = User.objects.create_user(
#                 username=username,
#                 password=password,
#                 email=email,
#                 )
# 
#         return redirect(
#                reverse(
#                    "auth:login" 
#                   ) 
#                 )
#     return render(
#            request,
#            "auth/signup.html",
#            {},
#            )
