from home.models import contact_us
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only, custom_login_required

# Create your views here


@custom_login_required
@admin_only
def viewMessage(request, id):
    messages_detail = contact_us.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})