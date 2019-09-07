from django.contrib import admin

from .models import Quote, Comment, Category

# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "quote", "author_quote", "publish_quote", "status")
    list_filter = ('status', 'created_quote', 'updated_quote', "author", "category")
    search_fields = ("author_quote", 'quote')

admin.site.register(Quote, QuoteAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)

admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "created", "updated")
    list_filter = ("created", "updated")
    search_fields = ("user", "comment")

admin.site.register(Comment, CommentAdmin)
