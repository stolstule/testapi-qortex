from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def str(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    def str(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    number = models.IntegerField()

    def str(self):
        return self.title