from django.shortcuts import render
from django.views import View
from Shorten_URL.forms import UrlForm

# Create your views here.


class UrlView(View):

    def get(self, request):
        form = UrlForm()
        return render(request, "url_form.html", {"form": form})
