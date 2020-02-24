from django.contrib import admin
from .models import User,Genre,Book,Reader,Quote

admin.site.register(User)
class BookAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'url_address', 'genre','created')
    list_filter = ['owner', 'title','genre' ]
    search_fields = ('owner','title',)
    ordering = ('created',)
admin.site.register(Book,BookAdmin)

admin.site.register(Reader)
admin.site.register(Genre)

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'from_writer', 'from_book', 'Overview','created')
    list_filter = ['owner', 'from_writer', 'from_book', 'Overview','created']
    search_fields = ('owner', 'from_writer', 'from_book',)
    ordering = ('created', )
admin.site.register(Quote,QuoteAdmin)

#from django.contrib.admin.models import LogEntry
#LogEntry.objects.all().delete()