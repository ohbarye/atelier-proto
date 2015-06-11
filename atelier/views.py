from django.shortcuts import render_to_response
from atelier.models import Album
import random

def index(request, image_type=''):
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
