import os
from dronzaPanel.models import EmailContent
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.conf import settings


class Communication_Utils():

    @classmethod
    def email_sender(cls, user, subject, message, html_message=None) -> object:
        try:
            from_email = 'Dronza <no_reply@dronza.org>'
            msg = EmailMultiAlternatives(subject, message, from_email, [user.email])
            img_content = Email_Content.get_image_contents('static/Assets/dronza_images/dronza_red.png')
            img_tag = '<img src= "cid:logo" width="200px"/>'
            html_message = img_tag + html_message
            msg.attach_alternative(html_message, "text/html")
            msg.attach(img_content)
            msg.send()
            return True
        except Exception as e:
            return False


class Email_Content():

    @classmethod
    def get_image_contents(cls, image_name):
        path_of_image = os.path.join(image_name)
        with open(path_of_image, 'rb') as f:
            logo_data = f.read()
        logo = MIMEImage(logo_data)
        logo.add_header('Content-ID', '<logo>')
        return logo

    @classmethod
    def welcome_email(cls, user):
        obj = EmailContent.objects.filter(name="welcome_email").first()
        if obj:
            subject = obj.subject
            message = obj.message
            html_message = obj.html_message
            html_message = html_message.format(user.username)
            return subject, message, html_message