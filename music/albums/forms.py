from django import forms
from .models import *


class AlbumsForm(forms.ModelForm):
    artist = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': 55}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': 55}))
    maker = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': 40}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'style': '7ch'}))
    cover = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))

    # cover = forms.FileField(required=True)
    # cover = forms.FileInput()

    class Meta:
        model = Album
        fields = '__all__'


class SongsForm(forms.ModelForm):
    track_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    track_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    track_artist = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    track_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'value': '00:00:00',
        'style': 'text-align: center!important'
    }))

    #     'class': 'form-control',
    #     'type': 'time',
    #     'step': '2',
    #     'value': '00:00:00'
    # }))

    class Meta:
        model = Song
        fields = ['track_no', 'track_name', 'track_artist', 'track_time']
        # fields = '__all__'

# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#
#     for field in self.Meta.required:
#         self.fields[field].required = True

# class Meta:
#     model = Album
#     fields = '__all__'
#     required = ('artist', 'name', 'year', 'cover')
#     widgets = {'artist': widgets.TextInput(attrs={'size': 55}),
#                'name': widgets.TextInput(attrs={'size': 55}),
#                'maker': widgets.TextInput(attrs={'size': 45}),
#                'year': widgets.NumberInput(attrs={'style': 'width:7ch'}),
#                'cover': widgets.FileInput()
#                }
# 'maker': widgets.TextInput(),
# class AlbumsForm(forms.Form):
#     artist = forms.CharField(label='Исполнитель', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     name = forms.CharField(label='Альбом', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     year = forms.IntegerField(label='Издан', widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     maker = forms.CharField(label='Издатель', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     photo = forms.ImageField(label='Обложка диска')
#
#     def clean(self):
#         super(AlbumsForm, self).clean()
#         return self.cleaned_data
