from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog, seoTags, MainSlider
from home.models import blog_Review
from django.urls import reverse


def blog(request, page_number=None):
    blog_data = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')
    paginator = Paginator(blog_data, 9)
    blog_data_final = paginator.get_page(page_number)
    total_pages = blog_data_final.paginator.num_pages

    recent_posts = userBlog.objects.order_by('-sNo')[:2]
    popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    featured_products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
    SMDT = SocialMedia.objects.all()
    SLIDER = MainSlider.objects.filter(page='blog_page')

    canonical_link = reverse('blog')  # Assuming 'blog' is the name of your URL pattern

    if page_number:
        canonical_link += f'/page/{page_number}'

    SEOTAGS = [{
        'title': "Latest Drone News, Tips, and Insights",
        'description': "Discover the latest tech drone information, news, and valuable insights Our blog covers everything related to drones, including industry updates",
        'tags': "Dronza Blog Drone News Drone Tips Drone Insights Drone Technology Drone Enthusiast Website Usage Top Products",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {
        'BLOGDATA': blog_data_final,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'RCPST': recent_posts,
        'Blog_RCPST': popular_posts,
        'Top_Products': featured_products,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER
    }
    return render(request, 'Blog.html', context)


def search_blog(request):
    search_keyword = request.GET.get('search_keyword') or request.POST.get('search_keyword')
    blog_data = userBlog.objects.all()  # Get all blog data initially

    if search_keyword:
        blog_data = blog_data.filter(
            Q(title__icontains=search_keyword) |
            Q(heading__icontains=search_keyword) |
            Q(description__icontains=search_keyword)
        ).values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')

    paginator = Paginator(blog_data, 9)
    page_number = request.GET.get('page')
    blog_data_final = paginator.get_page(page_number)
    total_pages = blog_data_final.paginator.num_pages

    recent_posts = userBlog.objects.order_by('-sNo')[:2]
    popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    featured_products = Products.objects.filter(featured='Featured').order_by('-id')[:4]

    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='search_blog')
    SLIDER = MainSlider.objects.filter(page='search_blog_page')

    context = {
        'SEARCHDATA': blog_data_final,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'RCPST': recent_posts,
        'Blog_RCPST': popular_posts,
        'Top_Products': featured_products,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS,
        'search_keyword': search_keyword,
        'SLIDER': SLIDER
    }
    return render(request, 'search_blog.html', context)


def postDetail(request, slug):
    rdPost = userBlog.objects.filter(slug=slug)
    comments = blog_Review.objects.filter(post__in=rdPost)
    Top_Products = Products.objects.filter(featured='Featured').order_by('-id')[:4]
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    popular_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    SMDT = SocialMedia.objects.all()
    SLIDER = MainSlider.objects.filter(page='blog_detail_page')
    SEOTAGS = [{'title': rdPost.first().title,
                'description': rdPost.first().description[:160],
                'tags': rdPost.first().title,
                'canonical_link': f'https://dronza.org/{rdPost.first().slug}'}]

    context = {
        'rdPost': rdPost,
        'RCPST': RCPST,
        'coments': comments,
        'Blog_RCPST': popular_posts,
        'Top_Products': Top_Products,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER
    }
    return render(request, 'postDetail.html', context)
