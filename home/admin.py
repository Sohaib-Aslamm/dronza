from django.contrib import admin
from home.models import *
from home.forms import ProductImageFormSet


@admin.register(contact_us)
class contact_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'subject', 'message')
    list_filter = ('name', 'email')
    search_fields = ['name', 'phone', 'email', 'subject', 'message']


@admin.register(productReview)
class productReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'email', 'review', 'timestamp')
    list_filter = ('product', 'email')
    search_fields = ['product', 'author', 'email', 'message', 'timestamp']
    date_hierarchy = 'timestamp'


class ProductImageInline(admin.TabularInline):
    model = sellYourDroneImages
    formset = ProductImageFormSet


@admin.register(sellYourDrone)
class sellYourDroneAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'status', 'is_featured')
    list_filter = ('user', 'email', 'status', 'is_featured', 'color')
    search_fields = ['user', 'email', 'address', 'location', 'title']
    autocomplete_fields = ('user', )
    ordering = ['name']
    inlines = [ProductImageInline]
    exclude = ['slug']


@admin.register(sellYourDroneImages)
class sellYourDroneImagesAdmin(admin.ModelAdmin):
    list_display = ('Product', 'image')
    list_filter = ('Product', )
    search_fields = ['Product', ]
    autocomplete_fields = ('Product', )

