from django.shortcuts import render
from django.views.generic import View, TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context["site_name"] = "seul blog"
        return context

# def home(request):
#     return render(
#            request,
#            "home.html",
#            {},
#            )
# class HomeView(View):
#     
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             "home.html",
#             {},
#         )
