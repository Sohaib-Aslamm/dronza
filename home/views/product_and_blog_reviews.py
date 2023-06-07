from django.shortcuts import redirect
from home.models import productReview, userBlog, blog_Review
from dronzaPanel.models import Products


def prodReview(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        author = request.POST.get('author')
        email = request.POST.get('email')
        review = request.POST.get('review')
        prd_id = Products.objects.get(slug=slug)
        sv = productReview(author=author, email=email, review=review, product=prd_id)
        sv.save()
        return redirect(f'/shop/{slug}')


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
