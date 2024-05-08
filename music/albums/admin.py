from django.contrib import admin
from .models import *


# from django.forms import widgets


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'name', 'year', 'maker', 'cover')
    list_display_links = ('artist', 'name')
    search_fields = ('artist', 'name')
    list_editable = ('cover',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}


@admin.register(Song)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('album_key', 'track_no', 'track_name', 'track_artist', 'length')
    list_display_links = ('track_name',)
    search_fields = ('track_name', 'track_artist')

    def length(self, obj):
        return obj.track_time.strftime('%H:%M:%S')

# admin.site.register(Albums, AlbumsAdmin)
# admin.site.register(Sounds, SoundsAdmin)
