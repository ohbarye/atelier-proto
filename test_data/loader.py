# -*- coding:utf-8 -*-
#
#    コマンドラインから下記を実行してインポートする
#
#    python manage.py shell
#    from test_data.loader import *
#    [method_name]()
#
#    ロードしたデータを削除するときは
#    from atelier.models import [model_class_name]
#    [model_class_name].objects.all().delete()
#
#   すべてのデータを消してやりなおす場合は
#   db.sqlite3 を削除し、
#   python manage.py migrate でDBを再作成する
#   ただし管理ユーザ等もすべて消えるので注意
#

import csv
from atelier.models import Artist,Album,ArtworkClass,AlbumArtworkClass

def load_artist():
    '''アーティストをロードする'''
    music_reader = csv.reader(open('test_data/imageInformation.csv', 'rb'))

    # 重複を削除
    artists = set([row[1] for row in music_reader])

    for artist_name in artists:
        artist = Artist(name=artist_name)
        artist.save()

def load_album():
    '''アルバムをロードする'''
    music_reader = csv.reader(open('test_data/imageInformation.csv', 'rb'))

    for row in music_reader:
        artist = Artist.objects.get(name=row[1])
        album = Album(seven_static_id=row[0],artist=artist,name=row[2],artwork_url=row[3])
        album.save()

def load_class():
    '''アートワークの分類をロードする'''
    class_reader = csv.reader(open('test_data/artwork_class.csv', 'rb'))

    for row in class_reader:
        class_id_number = int(row[0][1:])
        artwork_class = ArtworkClass(class_id=row[0],class_id_number=class_id_number,name=row[1],name_jp=row[2])
        artwork_class.save()

def load_recognition():
    '''アートワークの解析結果(分類)をロードする
    スコアが高い順に1〜3位まで記録する
    '''
    recognition_reader = csv.reader(open('test_data/recognition.csv', 'rb'))

    for row in recognition_reader:
        album = Album.objects.get(seven_static_id=row[0])
        artwork_class = ArtworkClass.objects.get(class_id=row[1])
        rank = AlbumArtworkClass.objects.filter(album__seven_static_id=row[0]).count() + 1

        recognition = AlbumArtworkClass(album=album,artwork_class=artwork_class,score_rank=rank,score=row[2])
        recognition.save()

def load_all():
    load_artist()
    load_album()
    load_class()
    load_recognition()
