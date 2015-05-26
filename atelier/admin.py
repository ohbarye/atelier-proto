from django.contrib import admin
from atelier.models import Artist, Album, ArtworkAttr, AlbumArtworkAttr

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(ArtworkAttr)
admin.site.register(AlbumArtworkAttr)
