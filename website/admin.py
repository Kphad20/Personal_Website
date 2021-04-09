from django.contrib import admin
from .models import Blog #, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Category, CategoryAdmin)

