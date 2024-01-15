from django.contrib import admin
from .models import Article
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class ArticleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget},
    }

admin.site.register(Article, ArticleModelAdmin)
