from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog, seoTags, MainSlider
from home.commands import Data_Logger
from home.enumerators import SOLD_STATUS, DJANGO_VIEWS
from home.models import blog_Review, sellYourDrone
from django.urls import reverse


def blog(request, page_number=None):
    try:
        paginator = Paginator(userBlog.objects.all().order_by('-sNo'), 9)
        blog_posts = paginator.get_page(page_number)
        canonical_link = reverse('blog')  # Assuming 'blog' is the name of your URL pattern

        if page_number:
            canonical_link += f'/page/{page_number}'

        seo_tags = [{
            'title': "Latest Drone News, Tips, and Insights",
            'description': "Discover the latest tech drone information, news, and valuable insights Our blog covers "
                           "everything related to drones, including industry updates",
            'tags': "Dronza Blog Drone News Drone Tips Drone Insights Drone Technology Drone Enthusiast Website Usage "
                    "Top Products",
            'canonical_link': request.build_absolute_uri(canonical_link)
        }]

        context = {
            'blog_posts': blog_posts,
            'lastPage': blog_posts.paginator.num_pages,
            'page_list': range(1, blog_posts.paginator.num_pages + 1),
            'popular_posts': userBlog.objects.all().order_by('-sNo')[10:16],
            'featured_products': sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE)[:6],
            'social_media': SocialMedia.objects.all(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'seo_tags': seo_tags,
            'main_slider': MainSlider.objects.filter(page='blog_page')
        }
        return render(request, 'Blog.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.BLOG, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')


def search_blog(request):
    try:
        search_keyword = request.GET.get('search_keyword') or request.POST.get('search_keyword')
        blog_posts = userBlog.objects.all()  # Get all blog data initially

        if search_keyword:
            blog_posts = blog_posts.filter(
                Q(title__icontains=search_keyword) |
                Q(heading__icontains=search_keyword) |
                Q(description__icontains=search_keyword)
            ).all().order_by('-sNo')

        paginator = Paginator(blog_posts, 9)
        page_number = paginator.get_page(request.GET.get('page'))

        context = {
            'search_data': paginator.get_page(request.GET.get('page')),
            'lastPage': page_number.paginator.num_pages,
            'page_list': range(1, page_number.paginator.num_pages + 1),
            'popular_posts': blog_posts.order_by('-sNo')[10:16],
            'featured_products': sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE)[:6],
            'social_media': SocialMedia.objects.all(),
            'recent_blog_post': blog_posts.order_by('-sNo')[:2],
            'seo_tags': seoTags.objects.filter(page='search_blog'),
            'search_keyword': search_keyword,
            'main_slider': MainSlider.objects.filter(page='search_blog_page')
        }
        return render(request, 'search_blog.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.SEARCH_BLOG, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')


def read_blog_post(request, slug):
    try:
        blog_post = userBlog.objects.filter(slug=slug)
        seo_tags = [{'title': blog_post.first().title if blog_post else None,
                     'description': f'Explore the latest insights on {blog_post.first().title}' if blog_post else None,
                     'tags': blog_post.first().title if blog_post else None,
                     'canonical_link': f'https://dronza.org/{blog_post.first().slug}' if blog_post else None}]

        context = {
            'blog_post': blog_post,
            'post_comments': blog_Review.objects.filter(post__in=blog_post),
            'popular_posts': userBlog.objects.all().order_by('-sNo')[10:16],
            'featured_products': sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE)[:6],
            'main_slider': MainSlider.objects.filter(page='blog_detail_page'),
            'social_media': SocialMedia.objects.all(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'seo_tags': seo_tags,
        }
        return render(request, 'postDetail.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.READ_BLOG, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
