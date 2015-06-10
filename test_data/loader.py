# -*- coding:utf-8 -*-

import csv
from atelier.models import Artist,Album

def load_artist():
    '''コマンドラインから下記を実行してインポートする

    python manage.py shell
    from test_data.loader import load_artist
    load_artist()

    ロードしたデータを削除するときは
    from atelier.models import Artist
    Artist.objects.all().delete()
    '''
    music_reader = csv.reader(open('test_data/imageInformation.csv', 'rb'))

    # 重複を削除
    artists = set([row[1] for row in music_reader])

    for artist_name in artists:
        artist = Artist(name=artist_name)
        artist.save()

def load_album():
    '''コマンドラインから下記を実行してインポートする

    python manage.py shell
    from test_data.loader import load_album
    load_album()

    ロードしたデータを削除するときは
    from atelier.models import Album
    Album.objects.all().delete()
    '''
    music_reader = csv.reader(open('test_data/imageInformation.csv', 'rb'))

    for row in music_reader:
        artist = Artist.objects.get(name=row[1])
        album = Album(seven_static_id=row[0],artist=artist,name=row[2],artwork_url=row[3])
        album.save()
