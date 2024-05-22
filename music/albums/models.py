from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def upload_cover(instance, filename):
    _, ext = filename.split('.')
    return '{artist}/{year}-{album}/cover.{ext}'.format(
        artist=instance.artist,
        year=instance.year,
        album=instance.name,
        ext=ext
    )


class RewriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


class Album(models.Model):
    artist = models.CharField(max_length=128, verbose_name='Испонитель')
    name = models.CharField(max_length=255, verbose_name='Название альбома')
    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(2050),
        ], default=1960, verbose_name='Издан')
    maker = models.CharField(max_length=40, verbose_name='Издатель')
    cover = models.ImageField(upload_to=upload_cover, storage=RewriteStorage(), verbose_name='Обложка')

    def __str__(self):
        return f'{self.artist} {self.year} "{self.name}"'

    def get_absolute_url(self):
        return self.pk

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['artist', 'year']


class Song(models.Model):
    album_key = models.ForeignKey(Album, related_name='songs', verbose_name='Album', on_delete=models.CASCADE)
    track_no = models.PositiveSmallIntegerField(default=None, verbose_name='Track')
    track_name = models.CharField(max_length=128, verbose_name='Song')
    track_artist = models.CharField(max_length=128, verbose_name='Artist')
    track_time = models.TimeField(default='00:00:00', verbose_name='Length')

    def __str__(self):
        # return self.track_time.strftime("%H:%M:%S")
        return str(self.pk)

    def get_absolute_url(self):
        return self.album_key

    #
    class Meta:
        verbose_name = 'Композиции'
        verbose_name_plural = 'Композиции'
        unique_together = ['album_key', 'track_no']
        ordering = ['track_no']
