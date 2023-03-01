from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.TextField(max_length=300, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
