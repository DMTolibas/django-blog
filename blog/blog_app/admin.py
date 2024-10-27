from django.contrib import admin

# Register your models here.
from .models import Author, Article, Feedback

admin.site.register(Author)
admin.site.register(Feedback)


    
#Filter and custom display of object in Admin view
class ArticleAdminFilter(admin.ModelAdmin):
    list_display = ("date_created", "title", "language", "status")


admin.site.register(Article, ArticleAdminFilter)
