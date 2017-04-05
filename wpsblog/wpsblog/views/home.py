from django.shortcuts import render
from django.views.generic import View


# def home(request):
#     return render(
#            request,
#            "home.html",
#            {},
#            )
class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "home.html",
            {},
        )
