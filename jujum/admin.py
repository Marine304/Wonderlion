from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class JujumAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(models.Jujum, JujumAdmin)
