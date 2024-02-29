import shutil
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import *
from .models import *


def index(request):
    context = dict(title='Главная страница')
    return render(request, 'albums/album_load.html', context)


def album_list(request):
    context = dict(title='Список альбомов', albums=Album.objects.all().order_by('artist'))
    return render(request, 'albums/album_list.html', context)


def album_create(request):
    if request.method == 'POST':
        form = AlbumsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'albumsChanged'})
    else:
        form = AlbumsForm()
        context = dict(form=form, title='Добавление нового альбома')
        return render(request, 'albums/album_form.html', context)


def cover_tree(album):
    return '.' + settings.MEDIA_URL + album.cover.name.rsplit('/cover.jpg', 1)[0]


def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    # tree_path = cover_tree(album)
    if request.method == 'POST':
        form = AlbumsForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            # if 'cover' in form.changed_data:
            # if form.has_changed():
            #     shutil.rmtree(tree_path, ignore_errors=False)
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'albumsChanged'})
    else:
        form = AlbumsForm(instance=album)
        context = dict(form=form, album=album, title='Редактирование альбома')
        return render(request, 'albums/album_form.html', context)


def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = dict(album=album, title='Подтверждение удаления')
    return render(request, 'albums/album_delete.html', context)


@require_POST
def album_remove(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tree_path = cover_tree(album)
    # album.cover.name.delete()
    shutil.rmtree(tree_path, ignore_errors=False)
    album.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'albumsChanged'})


def album_tracks(request, pk):
    context = {'album': get_object_or_404(Album, pk=pk)}
    return render(request, 'albums/track_list.html', context)


def tracks_add(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = SongsForm(request.POST)
        if form.is_valid():
            Song.objects.create(
                album_key=album,
                track_no=form.cleaned_data.get('track_no'),
                track_name=form.cleaned_data.get('track_name'),
                track_artist=form.cleaned_data.get('track_artist'),
                track_time=form.cleaned_data.get('track_time')
            )
            return redirect('album_tracks', pk=pk)
            # return HttpResponse(status=204, headers={'HX-Trigger': 'songsChanged'})
    else:
        form = SongsForm()
        context = dict(form=form, album=album, remove=False)
        return render(request, 'albums/track_form.html', context)


def song_update(request, item):
    song = get_object_or_404(Song, id=item)
    if request.method == 'POST':
        form = SongsForm(request.POST)
        if form.is_valid():
            Song.objects.filter(id=item).update(
                track_no=form.cleaned_data.get('track_no'),
                track_name=form.cleaned_data.get('track_name'),
                track_artist=form.cleaned_data.get('track_artist'),
                track_time=form.cleaned_data.get('track_time')
            )
            return redirect('album_tracks', pk=song.album_key.pk)
    else:
        form = SongsForm(initial={
            'track_no': song.track_no,
            'track_name': song.track_name,
            'track_artist': song.track_artist,
            'track_time': song.track_time
        })
        context = dict(form=form, album=song.album_key, remove=False)
        return render(request, 'albums/track_form.html', context)


def song_delete(request, item):
    song = get_object_or_404(Song, id=item)
    form = SongsForm(initial={
        'track_no': song.track_no,
        'track_name': song.track_name,
        'track_artist': song.track_artist,
        'track_time': song.track_time
    })
    if request.method == 'POST':
        song.delete()
        return redirect('album_tracks', pk=song.album_key.pk)
    else:
        context = dict(form=form, album=song.album_key, remove=True)
        return render(request, 'albums/track_form.html', context)
