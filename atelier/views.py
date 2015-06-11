from django.shortcuts import render_to_response
from atelier.models import Album,ArtworkClass,AlbumArtworkClass
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

def class_view(request, class_id=''):
    if not class_id:
        class_id = ''

    artwork_class = ArtworkClass.objects.get(class_id=class_id)
    album_artwork_class_list = AlbumArtworkClass.objects.filter(artwork_class__class_id=class_id).order_by('-score')

    return render_to_response('class_view.html',
                            {
                                'artwork_class': artwork_class,
                                'album_artwork_class_list': album_artwork_class_list,
                            })
