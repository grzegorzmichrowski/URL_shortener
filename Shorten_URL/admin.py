from django.contrib import admin
from Shorten_URL.models import Url

# Register your models here.


class UrlAdmin(admin.ModelAdmin):
    list_display = ("url", "short_url")


admin.site.register(Url, UrlAdmin)
