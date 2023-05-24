from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog
from home.models import blog_Review


def blog(request):
    BLOGDATA = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLOGDATA, 9)
    pageNo = request.GET.get('page')
    BLOGDATAFINAL = paginator.get_page(pageNo)
    totalPages = BLOGDATAFINAL.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    Blog_RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
    Top_Products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT, 'Blog_RCPST': Blog_RCPST, 'Top_Products': Top_Products,
               'latest_keywords': latest_keywords}
    return render(request, 'Blog.html', context)


def search_blog(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        BLOGDATA = userBlog.objects.filter(Q(title__icontains=search_keyword) | Q(heading__icontains=search_keyword) | Q(description__icontains=search_keyword)).order_by('-sNo')
        paginator = Paginator(BLOGDATA, 9)
        pageNo = request.GET.get('page')
        BLOGDATAFINAL = paginator.get_page(pageNo)
        totalPages = BLOGDATAFINAL.paginator.num_pages
        SMDT = SocialMedia.objects.all()
        Blog_RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
        Top_Products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
        context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
                   'RCPST': RCPST, 'SMDT': SMDT, 'Blog_RCPST': Blog_RCPST, 'Top_Products': Top_Products,
                   'latest_keywords': latest_keywords}
        return render(request, 'Blog.html', context)


def postDetail(request, sNo):
    rdPost = userBlog.objects.filter(sNo=sNo)
    coments = blog_Review.objects.filter(post__in=rdPost)
    SMDT = SocialMedia.objects.all()
    Blog_RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
    Top_Products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments, 'Blog_RCPST': Blog_RCPST,
               'Top_Products': Top_Products, 'latest_keywords': latest_keywords}
    return render(request, 'postDetail.html', context)