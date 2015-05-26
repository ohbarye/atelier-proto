from django.shortcuts import render_to_response
from atelier.models import Album, ImageType
import random

def index(request):

    image_type = random.choice(ImageType.choices())[0]
    album_list = Album.objects.filter(artwork_attr__image_type=image_type)

    return render_to_response('index.html',
                            {
                                'album_list': album_list,
                                'image_type': ImageType.labels[image_type],
                            })
