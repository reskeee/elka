from django.contrib import admin
from .models import Partners, PartnersImage


class PartnersImageInline(admin.TabularInline):
    model = PartnersImage
    extra = 1

@admin.register(Partners)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PartnersImageInline]
    list_display = ('name', 'description', 'main_image_preview')
    search_fields = ('name',)

    def main_image_preview(self, obj):
        if obj.main_image:
            return f'<img src="{obj.main_image.url}" width="100" height="100" />'
        return "Нет изображения"

    main_image_preview.allow_tags = True
    main_image_preview.short_description = "Основное изображение"