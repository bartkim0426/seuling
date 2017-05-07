from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from bitly.models import Bitlink



class BitlinkCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "bitly/new.html",
            context={}
        )

    def post(self, request, *args, **kwargs):
        original_url = request.POST.get('original_url')
        user = request.user

        bitlink = request.user.bitlink_set.create(
            original_url=original_url,        
        )
        

        return redirect(reverse('home'))
