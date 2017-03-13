from django.template import loader
from django.shortcuts import render

def home(request): 
    template = loader.get_template("home.html")
    return render(
           request, 
           "home.html",
           {"site_name":"seul's blog"},
            )
