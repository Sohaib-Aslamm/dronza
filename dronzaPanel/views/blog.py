from dronzaPanel.models import userBlog

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only
from django.core.paginator import Paginator


@login_required(login_url='/user-login')
@admin_only
def adminuser_blog(request):
    if request.method == 'POST':
        reg = userBlog(title=request.POST['title'], heading=request.POST['heading'], tags=request.POST['tags'],
                       quote=request.POST['quote'], quote_by=request.POST['quote_by'],
                       description=request.POST['editor1'],
                       Icon=request.FILES['icon'], created_at=request.POST['created_at'])
        reg.save()
        return redirect('/adminblog')
    else:
        BLGdata = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')
        paginator = Paginator(BLGdata, 10)
        pageNo = request.GET.get('page')
        BLGdataFINAL = paginator.get_page(pageNo)
        totalPages = paginator.num_pages
        pageList = range(1, totalPages + 1)
        context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': pageList}
        return render(request, 'adminBlog.html', context)
