from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, SocialMedia, \
    userBlog, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, WhatPeopleSay, OurPartner, \
    amazonProduct


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter user name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter valid mail to get notifications'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'choose password'}),
            'password2': forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
        }


class AboutTitlePostForm(forms.ModelForm):
    class Meta:
        model = AboutTitlePost
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'feature1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 2'}),
            'feature3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 3'}),
        }


class MainSliderForm(forms.ModelForm):
    class Meta:
        model = MainSlider
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'header': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter header'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$100'}),
        }


class HomeHIWForm(forms.ModelForm):
    class Meta:
        model = HomeHIW
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }


class HomeHTUForm(forms.ModelForm):
    class Meta:
        model = HomeHTU
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }


class HomeAboutForm(forms.ModelForm):
    class Meta:
        model = HomeAbout
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'feature1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 1'}),
            'feature2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 2'}),
            'feature3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 3'}),
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'cPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'current price'}),
            'dPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'discounted price'}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$USD, PKR'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blue, Red, Black'}),
            'label1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'input1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }


class amazonProductsForm(forms.ModelForm):
    class Meta:
        model = amazonProduct
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'cPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter current price'}),
            'dPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter discounter price'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blue, Red, Black'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.Select(attrs={'class': 'form-control'}),
            'label1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'label6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'label'}),
            'input1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'input6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'buyLink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter buying link'}),
        }


class QualityTrustForm(forms.ModelForm):
    class Meta:
        model = QualityTrust
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }


class HomeSRFPForm(forms.ModelForm):
    class Meta:
        model = HomeSRFP
        fields = '__all__'

        widgets = {
            'satisfied_clients': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 60 or 70'}),
            'resolution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 4K , 8K'}),
            'flight_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 45 minute'}),
            'project_done': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 100'}),
        }


class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = '__all__'

        widgets = {
            'video_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter video link'}),
        }


class WhatPeopleSForm(forms.ModelForm):
    class Meta:
        model = WhatPeopleSay
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your designation'}),
            'say_something': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say Something'}),
        }


class OurPartnerForm(forms.ModelForm):
    class Meta:
        model = OurPartner
        fields = '__all__'

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'company introduction'}),
        }


class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'team member name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'member designation'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'member@dronza.org'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+92 xxx xxxxxxx'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5+ Year'}),
            'socialmedia1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Linkedin'}),
            'socialmedia2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
            'socialmedia3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write member detail...'}),
        }


class ServicesTypeForm(forms.ModelForm):
    class Meta:
        model = ServicesTypes
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write quote'}),
            'quote_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'quote author'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'highlight1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 1'}),
            'highlight2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 2'}),
            'highlight3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 3'}),
            'highlight4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 4'}),
            'highlight5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 5'}),
            'highlight6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 6'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter price $100'}),
            'feature1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
        }



class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'Category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

        }


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'skype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter skype'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+92) 344 4276747'}),
            'github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste github link'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste linkedin link'}),
            'google_plus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste google+ link'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste youtube link'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste facebook link'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste twitter link'}),
        }


class userBlogForm(forms.ModelForm):
    class Meta:
        model = userBlog
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter heading'}),
            'tags': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'enter tags ex. (IT, Business, Accounts)'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter a "Quote" regarding post'}),
            'quote_by': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'who said this quote ex. (sohaib_langrial)'}),


        }