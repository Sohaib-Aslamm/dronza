from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from home.models import sellYourDrone


def admin_seller_products(request):
    all_products_list = sellYourDrone.objects.all().order_by('-id')
    user_ids = [user.user_id for user in all_products_list]
    all_user_list = User.objects.filter(id__in=user_ids)

    paginator = Paginator(all_user_list, 10)
    pageNo = request.GET.get('page')
    all_user_list_final = paginator.get_page(pageNo)
    totalPages = paginator.num_pages
    pageList = range(1, totalPages + 1)
    context = {'all_user_list': all_user_list_final, 'lastPage': totalPages, 'pageList': pageList,
               'all_products_list': all_products_list}

    return render(request, 'admin_seller_list.html', context)
