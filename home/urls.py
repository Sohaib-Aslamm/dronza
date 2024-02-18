from django.urls import path
from home import views

urlpatterns = [

    path('', views.index, name="Home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('gallery', views.gallery, name="gallery"),
    path('customer-product', views.customer_product, name="customer-product"),
    path('blog', views.blog, name="blog"),
    path('search-blog', views.search_blog, name="search-blog"),
    path('contact-us', views.contactus, name="contact-us"),
    path('sell-drones', views.sellDrones, name="sell-drones"),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('blogReview', views.blog_post_review, name="blogReview"),
    path('thank-you', views.thankyou, name="thank-you"),
    path('search-by-location', views.search_by_location_category, name='search-by-location'),
    path('coming-soon', views.coming_soon, name="coming-soon"),
    path('error-404', views.error_404, name="error-404"),
    path('bad-request', views.general_error, name="bad-request"),

    path('user-login', views.user_login, name="user-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('register', views.user_registration, name="register"),
    path('news-letter', views.news_letter_subscriber, name="news-letter"),
    path('blog/page/<int:page_number>', views.blog, name="blog_page"),
    path('sell-drones/page/<int:page_number>', views.sellDrones, name="sell_drones_page"),
    path('customer-product/page/<int:page_number>', views.customer_product, name="customer_product_page"),
    path('<str:slug>', views.read_blog_post, name="read_blog_post"),
    path('<str:record_type>/<str:slug>', views.get_instance_detail, name="DetailRecord"),
    path('<str:record_type>/<str:slug>/delete', views.delete_record_by_uuid, name="Delete_with_diuu"),
    path('<str:record_type>/<str:slug>/update', views.update_record_by_uuid, name="Update_with_diuu"),




]
