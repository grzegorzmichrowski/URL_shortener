from django.db import models

# Create your models here.


class Url(models.Model):
    url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=20)
    short = models.IntegerField(null=True)

    def __str__(self):
        return self.url + f"({self.short_url})"
