from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from .models import Article, Category
from tinymce.widgets import TinyMCE

class articleAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'date', 'slug')
    search_fields = ('title',)
    exclude = ('slug',)
    filter_horizontal = ('category',)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    #prepopulated_fields = {'slug': ('title',)}    

class categoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Article, articleAdmin)
admin.site.register(Category, categoryAdmin)
