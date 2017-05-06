from django.views.generic import View
from django.http import HttpResponse


class PricingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Pricing Table")
