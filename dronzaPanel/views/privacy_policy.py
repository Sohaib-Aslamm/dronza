from dronzaPanel.models import PrivacyPolicy

from django.shortcuts import render, redirect

from dronzaPanel.decorators import admin_only, custom_login_required


@custom_login_required
@admin_only
def privacy_policy(request):
    if request.method == 'POST':
        reg = PrivacyPolicy(title=request.POST['title'], heading=request.POST['heading'],
                            description=request.POST['editor1'])
        reg.save()
        return redirect('/adminprivacypolicy')

    privacy_data = PrivacyPolicy.objects.all()
    return render(request, 'adminPrivacyPolicy.html', {'privacy_data': privacy_data})
