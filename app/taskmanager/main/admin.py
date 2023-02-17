from django.contrib import admin
from .models import Symptoms, Diseases, Causes, Questions


@admin.register(Diseases)
class DiseaseAdmin(admin.ModelAdmin):
    filter_horizontal = ['symptoms', 'causes']
    list_filter = ['title']
    search_fields = ['name']


admin.site.register(Symptoms)

admin.site.register(Causes)

admin.site.register(Questions)
