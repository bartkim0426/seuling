from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse 


def signup(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(
                username = username,
                password = password,
                )

    return redirect(
           reverse(
               "auth:login" 
              ) 
            )
