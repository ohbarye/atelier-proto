# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from atelier.models import Album,ArtworkClass,AlbumArtworkClass
from atelier.forms import SearchClassForm

def index(request, image_type=''):
    album_list = Album.objects.filter(artwork_attr__image_type=image_type)
    return render_to_response('index.html',
                            {   'album_list': album_list,
                                'selected_image_type': None,
                                'image_type_list': None,    })

def get_all_class(request):
    '''全クラス情報を取得するAPI'''
    cls_list = [c.serialize() for c in ArtworkClass.objects.all()]
    return render_json_response(request, cls_list)

def get_class_by_id(request):
    '''IDを指定してクラス情報を取得するAPI'''
    cls_id = request.GET["classId"]
    cls = ArtworkClass.objects.get(class_id=cls_id)
    return render_json_response(request, cls.serialize())

def get_artworks(request):
    '''Class IDを指定してAlbumリストを取得するAPI'''
    cls_id = request.GET['classId']
    rank   = request.GET['rankThres']  if 'rankThres'  in request.GET else 3
    score  = request.GET['scoreThres'] if 'scoreThres' in request.GET else 0

    aw_class = ArtworkClass.objects.get(class_id=cls_id)
    data = OrderedDict([
            ('class', aw_class.serialize()),
            ('album_list', [a.serialize() for a in get_artworks_by_class_id(aw_class,rank,score)])
        ])
    return render_json_response(request, data)

def get_artworks_by_class_id(aw_class,rank,score):
    return AlbumArtworkClass.objects.filter(
        artwork_class__class_id_number=aw_class.class_id_number,score_rank__lte=rank,score__gte=score).order_by('-score')

def get_album_artwork_class_lists(id_from,id_to,rank,score,omit_zero):
    lists = []
    for aw_class in ArtworkClass.objects.filter(class_id_number__range=(id_from,id_to)):
        aac = get_artworks_by_class_id(aw_class,rank,score)
        if not omit_zero or len(aac) > 0:
            lists.append(   {   'class': aw_class,
                                'list': aac         })
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
                                    {   'class_lists': class_lists,
                                        'form': form,   })
    else:
        form = SearchClassForm()

    return render_to_response('class_view.html', {
        'form': form,
    })

def class_list_view(request):
    return render_to_response('class_list_view.html',
                {'class_list': ArtworkClass.objects.all(),})

def main_view(request):
    return render_to_response('ParodyRecordAtelier.html')

def render_json_response(request, data, status=None):
    '''response を JSON で返却'''
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.REQUEST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response
