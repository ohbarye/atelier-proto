from django.contrib import admin
from atelier.models import Artist, Album, ArtworkClass, AlbumArtworkClass

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(ArtworkClass)
admin.site.register(AlbumArtworkClass)
