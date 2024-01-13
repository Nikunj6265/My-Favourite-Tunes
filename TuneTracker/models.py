from django.db import models


class Artist(models.Model):
    """
    Model representing an artist in the music collection.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    """
    Model representing a song in the music collection.
    """
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music_files')

    def __str__(self):
        return self.title