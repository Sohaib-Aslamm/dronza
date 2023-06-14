from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog, seoTags
from home.models import blog_Review


def blog(request):
    blog_data = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')
    paginator = Paginator(blog_data, 9)
    page_number = request.GET.get('page')
    blog_data_final = paginator.get_page(page_number)
    total_pages = blog_data_final.paginator.num_pages

    recent_posts = userBlog.objects.order_by('-sNo')[:2]
    popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    featured_products = Products.objects.filter(featured='Featured').order_by('-id')[:4]

    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='blog_page')

    context = {
        'BLOGDATA': blog_data_final,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'RCPST': recent_posts,
        'Blog_RCPST': popular_posts,
        'Top_Products': featured_products,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }
    return render(request, 'Blog.html', context)


def search_blog(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        blog_data = userBlog.objects.filter(Q(title__icontains=search_keyword) | Q(heading__icontains=search_keyword) | Q(description__icontains=search_keyword)).values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')
        paginator = Paginator(blog_data, 9)
        page_number = request.GET.get('page')
        blog_data_final = paginator.get_page(page_number)
        total_pages = blog_data_final.paginator.num_pages

        recent_posts = userBlog.objects.order_by('-sNo')[:2]
        popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
        featured_products = Products.objects.filter(featured='Featured').order_by('-id')[:4]

        SMDT = SocialMedia.objects.all()
        SEOTAGS = seoTags.objects.filter(page='search_blog')

        context = {
            'BLOGDATA': blog_data_final,
            'lastPage': total_pages,
            'pageList': range(1, total_pages + 1),
            'RCPST': recent_posts,
            'Blog_RCPST': popular_posts,
            'Top_Products': featured_products,
            'SMDT': SMDT,
            'SEOTAGS': SEOTAGS
        }
        return render(request, 'Blog.html', context)


def postDetail(request, slug):
    rdPost = userBlog.objects.filter(slug=slug)
    comments = blog_Review.objects.filter(post__in=rdPost)
    Top_Products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = [{'title': rdPost.first().title,
                'description': rdPost.first().title,
                'tags': rdPost.first().tags,
                'canonical_link': f'https://dronza.org/{rdPost.first().title}'}]

    context = {
        'rdPost': rdPost,
        'RCPST': RCPST,
        'coments': comments,
        'Blog_RCPST': popular_posts,
        'Top_Products': Top_Products,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }
    return render(request, 'postDetail.html', context)
