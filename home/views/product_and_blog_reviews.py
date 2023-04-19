from django.shortcuts import redirect
from home.models import productReview, userBlog, blog_Review
from dronzaPanel.models import Products


def prodReview(request):
    if request.method == 'POST':
        prdSno = request.POST.get('pdsNo')
        pdUUID = request.POST.get('pdUUID')
        author = request.POST.get('author')
        email = request.POST.get('email')
        review = request.POST.get('review')
        prd_id = Products.objects.get(id=prdSno)
        sv = productReview(author=author, email=email, review=review, product=prd_id)
        sv.save()
        return redirect(f'/shopDetail/{prdSno}/{pdUUID}/dronzaProduct')


def blogReview(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = userBlog.objects.get(sNo=postSno)
        sv = blog_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()
        return redirect(f'/postDetail/{postSno}')