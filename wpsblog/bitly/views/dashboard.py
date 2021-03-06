from django.shortcuts import render
from django.views.generic import View

from bitly.models import Bitlink


class BitlinkDashboardView(View):

    def get(self, request, *args, **kwargs):

        bitlink = Bitlink.objects.get(
            shorten_hash=kwargs.get("shorten_hash")
        )

        return render(
            request,
            "bitly/dashboard.html",
            context={"bitlink": bitlink},
        )
