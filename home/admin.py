from django.contrib import admin
from home.models import *
from home.forms import ProductImageFormSet


@admin.register(contact_us)
class contact_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'subject', 'message')
    list_filter = ('name', 'email')
    search_fields = ['name', 'phone', 'email', 'subject', 'message']


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


@admin.register(blog_Review)
class blog_ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'comment', 'post', 'timestamp')
    list_filter = ('author', 'email')
    search_fields = ['author', 'email', 'comment', 'timestamp']
    autocomplete_fields = ('post', )


@admin.register(NewsLetterSubscriber)
class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')
    list_filter = ('email',)
    search_fields = ['email', 'timestamp']
