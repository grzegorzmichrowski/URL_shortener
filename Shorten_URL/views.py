from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.views import View
from Shorten_URL.forms import UrlForm
from Shorten_URL.models import Url
import random

# Create your views here.


SHORTS = list(range(1, 10000))


class UrlView(View):

    def get(self, request):
        form = UrlForm()
        return render(request, "url_form.html", {"form": form})

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            random_number = random.choice(SHORTS)
            short = str(SHORTS.pop(random_number))
            short_url = str(get_current_site(request)) + "/" + short
            Url.objects.create(url=url,
                               short_url=short_url,
                               short=short)
            return render(request, "short_url.html", {"short_url": short_url, "url": url})


class ShortUrlView(View):

    def get(self, request, short):
        obj = Url.objects.get(short=short)
        return redirect(obj.url)
