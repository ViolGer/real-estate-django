from django.contrib import admin
from django.utils.html import format_html  # нужно для генерации HTML в админке
from django.http import HttpResponse
from .models import Property, PropertyImage
import csv

#для отображения галереи в админке
#TabularInline это табличный вид
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage #модель изображений
    extra = 1 #показывать 1 пустое поле для загрузки по умолчанию

# Класс настройки отображения модели в админке
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # Какие поля показывать в списке объектов
    list_display = ('title', 'city', 'country', 'price', 'currency', 'is_available', 'created_at', 'owner')
    # Фильтры в правой части админки
    list_filter = ('country', 'city', 'is_available')
    # Поля, по которым можно искать через строку поиска
    search_fields = ('title', 'description', 'city', 'country')
    #возможность добавлять несколько картинок через встроенную модель
    inlines = [PropertyImageInline]
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # создаём HTTP-ответ с типом "CSV"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=properties.csv'

        writer = csv.writer(response)

        # первая строка — заголовки колонок
        writer.writerow(['Title', 'City', 'Country', 'Price', 'Currency', 'Available', 'Created At'])

        # далее — по каждой строке из выборки
        for prop in queryset:
            writer.writerow([
                prop.title,
                prop.city,
                prop.country,
                prop.price,
                prop.currency,
                '✅' if prop.is_available else '❌',
                prop.created_at.strftime('%Y-%m-%d')
            ])

        return response

    export_as_csv.short_description = "📥 Скачать как CSV"

#админка для изображений с миниатюрой
@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'thumbnail', 'caption')  # показываем картинку и подпись

    # Метод, чтобы отобразить картинку
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.image.url)
        return "-"
    thumbnail.short_description = "Превью"  # заголовок столбца


