from django.contrib import admin
from .models import Disc
# Register your models here.

class DiscAdmin(admin.ModelAdmin):
    list_display = ('artist', 'album', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {"slug": ("artist", "album")}

admin.site.register(Disc, DiscAdmin)
