from django.forms import ModelForm
from Shorten_URL.models import Url


class UrlForm(ModelForm):

    class Meta:
        model = Url
        fields = ["url", ]

