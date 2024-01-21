from django.shortcuts import redirect
from home.models import userBlog, blog_Review


def blogReview(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post = userBlog.objects.get(slug=slug)
        sv = blog_Review(author=author, email=email, comment=comment, post=post)
        sv.save()
        return redirect(f'/{slug}')
