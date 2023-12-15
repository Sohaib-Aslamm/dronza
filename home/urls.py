from django.urls import path
from home import views


urlpatterns = [

    path('', views.index, name="Home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('gallery', views.gallery, name="gallery"),
    path('shop', views.shop, name="shop"),
    path('customer-product', views.customerProduct, name="customer-product"),
    path('blog', views.blog, name="blog"),
    path('search-blog', views.search_blog, name="search-blog"),
    path('contact-us', views.contactus, name="contact-us"),
    path('sell-drones', views.sellDrones, name="sell-drones"),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('prodReview', views.prodReview, name="prodReview"),
    path('blogReview', views.blogReview, name="blogReview"),
    path('thank-you', views.thankyou, name="thank-you"),

    # path('order-placed', views.orderDone, name="order-placed"),
    # path('track-order', views.trackOrder, name='track-order'),
    # path('cart/add/<int:id>', views.cart_add, name='cart_add'),
    # path('cart/item_clear/<int:id>', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:id>', views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>', views.item_decrement, name='item_decrement'),
    # path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart-detail', views.cart_detail, name='cart-detail'),
    # path('checkout', views.checkout, name='checkout'),
    # path('place-order', views.place_order, name='place-order'),
    # path('shop/page/<int:page_number>', views.shop, name="shop_page"),

    path('search-by-location', views.search_by_location, name='search-by-location'),
    path('coming-soon', views.coming_soon, name="coming-soon"),
    path('blog/page/<int:page_number>', views.blog, name="blog_page"),

    path('sell-drones/page/<int:page_number>', views.sellDrones, name="sell_drones_page"),
    path('customer-product/page/<int:page_number>', views.customerProduct, name="customer_product_page"),
    path('<str:slug>', views.postDetail, name="postDetail"),
    path('<str:type>/<str:slug>', views.DetailRecord, name="DetailRecord"),
    path('<str:type>/<str:slug>/delete', views.DeletebyUUID, name="Delete_with_diuu"),
    path('<str:type>/<str:slug>/update', views.UpdatebyUUID, name="Update_with_diuu"),


]
