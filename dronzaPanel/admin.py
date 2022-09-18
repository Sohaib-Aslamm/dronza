from django.contrib import admin
from dronzaPanel.models import *
# Register your models here.


class Dronza(admin.ModelAdmin):
    pass

admin.site.register(MainSlider, Dronza)
admin.site.register(HomeHIW, Dronza)
admin.site.register(HomeHTU, Dronza)
admin.site.register(HomeAbout, Dronza)
admin.site.register(Products, Dronza)
admin.site.register(productImages, Dronza)
admin.site.register(amazonProduct, Dronza)
admin.site.register(amazonProductImages, Dronza)
admin.site.register(HomeSRFP, Dronza)
admin.site.register(VideoGallery, Dronza)
admin.site.register(WhatPeopleSay, Dronza)
admin.site.register(OurPartner, Dronza)
admin.site.register(AboutTitlePost, Dronza)
admin.site.register(QualityTrust, Dronza)
admin.site.register(OurTeam, Dronza)
admin.site.register(ServicesTypes, Dronza)
admin.site.register(Pricing, Dronza)
admin.site.register(Gallery, Dronza)
admin.site.register(SocialMedia, Dronza)
admin.site.register(userBlog, Dronza)
