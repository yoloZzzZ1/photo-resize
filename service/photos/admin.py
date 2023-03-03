from django.contrib import admin

from django.contrib import admin
from .models.photos import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'filename',
        'processing',
        'processing_success',
    )

    list_display_links = (
        'filename',
    )
