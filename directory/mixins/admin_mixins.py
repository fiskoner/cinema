from django.contrib import admin
from django.utils.safestring import mark_safe


class ImageInlineMixin(admin.TabularInline):
    readonly_fields = ('image_preview',)
    extra = 1

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="200" height="200" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return '(No image)'