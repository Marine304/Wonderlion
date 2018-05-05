from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class NanjangAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(models.Nanjang, NanjangAdmin)
