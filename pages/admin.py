from django.contrib import admin
from .models import CodingGame

class CodingGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'difficulty', 'is_enabled')
    search_fields = ['title', 'description'] 
    
admin.site.register(CodingGame, CodingGameAdmin)
