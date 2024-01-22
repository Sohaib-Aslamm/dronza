from django.contrib import admin
from dronzaPanel.models import *


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'image', 'background_image')
    list_filter = ('title', 'page')
    search_fields = ['title', 'page']


@admin.register(HomeHIW)
class HomeHIWAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', )
    search_fields = ['title', 'description']


@admin.register(HomeHTU)
class HomeHTUAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', )
    search_fields = ['title', 'description']


@admin.register(HomeAbout)
class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    list_filter = ('title',)
    search_fields = ['title', 'description']


@admin.register(HomeSRFP)
class HomeSRFPAdmin(admin.ModelAdmin):
    list_display = ('satisfied_clients', 'resolution', 'flight_time', 'project_done')


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('video_link', 'icon')


@admin.register(WhatPeopleSay)
class WhatPeopleSayAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'say_something', 'icon')
    list_filter = ('name', 'designation')
    search_fields = ['name', 'designation']


@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'description', 'logo')


@admin.register(AboutTitlePost)
class AboutTitlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'feature1', 'feature2', 'feature3', 'image')
    list_filter = ('title', )
    search_fields = ['title', 'description']


@admin.register(QualityTrust)
class QualityTrustAdmin(admin.ModelAdmin):
    list_display = ('title', 'Description', 'icon')
    list_filter = ('title', )
    search_fields = ['title', 'description']


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'experience', 'designation', 'description', 'profile',
                    'socialmedia1', 'socialmedia2', 'socialmedia3')
    list_filter = ('name', 'designation')
    search_fields = ['name', 'email', 'experience', 'designation', 'description']

    exclude = ['slug']


@admin.register(ServicesTypes)
class ServicesTypesAdmin(admin.ModelAdmin):
    list_display = ('title', 'Description', 'type', 'icons')
    list_filter = ('title', 'type')
    search_fields = ['title', 'Description', 'type']

    exclude = ['slug']


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('category', 'price')
    list_filter = ('category', 'price')
    search_fields = ['category', 'price']


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading', 'description')
    list_filter = ('title', 'heading')
    search_fields = ['title', 'heading', 'description']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'image')
    list_filter = ('title', 'category')
    search_fields = ['title', 'category', 'description']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('email', 'skype', 'phone', 'github', 'linkedin', 'google_plus', 'youtube', 'facebook', 'twitter')
    list_filter = ('email', 'phone',)
    search_fields = ['email', 'skype', 'phone', 'github', 'linkedin', 'google_plus', 'youtube', 'facebook', 'twitter']


@admin.register(userBlog)
class userBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading', 'description', 'Icon', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ['title', 'heading', 'description', 'created_at']
    date_hierarchy = 'created_at'

    exclude = ['slug']


@admin.register(seoTags)
class seoTagsAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'canonical_link', 'description', 'tags')
    list_filter = ('title', 'page',)
    search_fields = ['title', 'page', 'canonical_link', 'description', 'tags']


@admin.register(EmailContent)
class EmailContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'html_message')
    list_filter = ('name',)
    search_fields = ['name', 'subject', 'html_message']

    exclude = ['slug']