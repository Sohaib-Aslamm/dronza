from dronzaPanel.models import userBlog

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only
from django.core.paginator import Paginator


@login_required(login_url='/user_login')
@admin_only
def adminuser_blog(request):
    if request.method == 'POST':
        TIT = request.POST.get('title')
        HD = request.POST.get('heading')
        TGS = request.POST.get('tags')
        QT = request.POST.get('quote')
        QTBY = request.POST.get('quote_by')
        CRA = request.POST.get('created_at')
        DSC = request.POST.get('editor1')
        ICN = request.FILES['icon']
        reg = userBlog(title=TIT, heading=HD, tags=TGS, quote=QT, quote_by=QTBY, description=DSC, Icon=ICN,
                       created_at=CRA)
        reg.save()

    paginator = Paginator(userBlog.objects.order_by('-sNo'), 10)
    pageNo = request.GET.get('page')
    BLGdataFINAL = paginator.get_page(pageNo)
    totalPages = paginator.num_pages
    pageList = range(1, totalPages + 1)
    context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': pageList}
    return render(request, 'adminBlog.html', context)
