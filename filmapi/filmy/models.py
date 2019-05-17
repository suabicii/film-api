from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    year = models.IntegerField(default=1900)
    poster = models.ImageField(upload_to='plakaty', default=None)

    def __str__(self):
        return self.title