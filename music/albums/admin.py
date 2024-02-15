from django.contrib import admin
from .models import *
# from django.forms import widgets


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'name', 'year', 'maker', 'cover')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    list_editable = ('cover',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}

@admin.register(Song)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('album_key', 'track_no', 'track_name', 'track_artist', 'track_time')

    # def track_time(self, obj):
    #     return obj.timefield.strftime('%H:%M%:%S')
        # return obj.result_value.strftime('%H:%M%:%S')
    #
    # formfield_overrides = {
    #     models.TimeField: {'widget': widgets.TimeInput(format='%H:%M:%S')},
    # }

# admin.site.register(Albums, AlbumsAdmin)
# admin.site.register(Sounds, SoundsAdmin)
