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
            html_message = html_message
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            return True
        except Exception as e:
            return False


class Email_Content():
    @classmethod
    def welcome_email(cls, user):
        obj = EmailContent.objects.filter(name="welcome_email").first()
        if obj:
            subject = obj.subject
            message = obj.message
            html_message = obj.html_message
            html_message = html_message.format(user.username)
            return subject, message, html_message