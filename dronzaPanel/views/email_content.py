from dronzaPanel.forms import EmailContentForm
from dronzaPanel.models import EmailContent

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required


@custom_login_required
@admin_only
def admin_email_content(request):
    if request.method == 'POST':
        email_form = EmailContentForm(request.POST, request.FILES)
        if email_form.is_valid():
            name = email_form.cleaned_data['name']
            subject = email_form.cleaned_data['subject']
            text_message = email_form.cleaned_data['message']
            html_message = email_form.cleaned_data['html_message']

            register = EmailContent(name=name, subject=subject, message=text_message, html_message=html_message)
            register.save()
            email_form = EmailContentForm()
    else:
        email_form = EmailContentForm()
    email_data = EmailContent.objects.all()
    return render(request, 'admin_email_content.html', {'form': email_form, 'email_data': email_data})
