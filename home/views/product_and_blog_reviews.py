from django.shortcuts import redirect

from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS
from home.models import blog_Review
from dronzaPanel.models import userBlog


def blog_post_review(request):
    try:
        if request.method == 'POST':
            slug = request.POST.get('slug')
            author = request.POST.get('author')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            post = userBlog.objects.get(slug=slug)
            sv = blog_Review(author=author, email=email, comment=comment, post=post)
            sv.save()
            return redirect(f'/{slug}')
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.BLOG_REVIEWS, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
