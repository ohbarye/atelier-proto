# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from atelier.models import Album,ArtworkClass,AlbumArtworkClass
from atelier.forms import SearchClassForm
import random

def index(request, image_type=''):

    album_list = Album.objects.filter(artwork_attr__image_type=image_type)

    return render_to_response('index.html',
                            {
                                'album_list': album_list,
                                'selected_image_type': None,
                                'image_type_list': None,
                            })


'''
    if not image_type:
        image_type = random.choice(ImageType.choices())[0]

    album_list = Album.objects.filter(artwork_attr__image_type=image_type)

    return render_to_response('index.html',
                            {
                                'album_list': album_list,
                                'selected_image_type': ImageType.labels[int(image_type)],
                                'image_type_list': ImageType.choices(),
                            })
'''

def class_list_view(request):
    return render_to_response('class_list_view.html',
                            {
                                'class_list': ArtworkClass.objects.all(),
                            })


def get_album_artwork_class_lists(id_from,id_to,rank,score,omit_zero):
    aw_classes = ArtworkClass.objects.filter(class_id_number__range=(id_from,id_to))

    lists = []
    for aw_class in aw_classes:
        aac = AlbumArtworkClass.objects.filter(artwork_class__class_id_number=aw_class.class_id_number,score_rank__lte=rank,score__gte=score).order_by('-score')
        if not omit_zero or len(aac) > 0:
            lists.append(
                {   'class': aw_class,
                    'list': aac
                    }
                )

    return lists

def class_view(request):

    if request.method == 'POST':

        form = SearchClassForm(request.POST)

        if form.is_valid():
            id_from = form.cleaned_data['class_id_from']
            id_to   = form.cleaned_data['class_id_to']
            rank    = form.cleaned_data['rank_threshold']
            score   = form.cleaned_data['score_threshold']
            omit_zero = form.cleaned_data['omit_zero_count']

            class_lists = get_album_artwork_class_lists(id_from,id_to,rank,score,omit_zero)

            return render_to_response('class_view.html',
                                    {
                                        'class_lists': class_lists,
                                        'form': form,
                                    })

    else:
        form = SearchClassForm()

    return render_to_response('class_view.html', {
        'form': form,
    })
