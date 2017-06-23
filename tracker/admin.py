from django.contrib import admin
from .models import Book
from .models import DVD
from .models import Mags
from .models import Newspaper
from .models import Music
from .models import Item



#class BookInline(admin.StackedInline):
    #model = Book

#class MagInline(admin.StackedInline):
 #   model = Mags

#class NewsInline(admin.StackedInline):
 #   model = Newspaper

#class DVDInline(admin.StackedInline):
  #  model = DVD

#class MusicInline(admin.StackedInline):
 #   model = Music

#class ItemAdmin(admin.ModelAdmin):
 #   inlines = [BookInline, NewsInline, DVDInline, MagInline, MusicInline]

  #  def item_type(self):
   #    if hasattr(self,'book'): return 'Book'
  #      if hasattr(self,'music'): return 'Music'
   #     if hasattr(self,'newspaper'): return 'Newspaper'
    #    if hasattr(self,'mags'): return 'Magazine'
     #   if hasattr(self,'dvd'): return 'DVD'

#    list_display = ['name', 'description', item_type]


admin.site.register(Item)
#admin.site.register(ItemAdmin)
admin.site.register(Book)
admin.site.register(DVD)
admin.site.register(Music)
admin.site.register(Mags)
admin.site.register(Newspaper)

##class DVDAdmin(admin.ModelAdmin):
  ##  prepopulated_fields = {'slug':('name',)}

