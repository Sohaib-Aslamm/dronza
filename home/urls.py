from django.urls import path
from home import views


urlpatterns = [

 path('', views.index, name="Home"),
    path('home', views.index, name="Home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('gallery', views.gallery, name="gallery"),
    path('shop', views.shop, name="shop"),
    path('customerProduct', views.customerProduct, name="customerProduct"),
    path('blog', views.blog, name="blog"),
    path('search_blog', views.search_blog, name="search_blog"),
    path('contactUs', views.contactus, name="contactus"),
    path('sellDrones', views.sellDrones, name="sellDrones"),
    path('prodReview', views.prodReview, name="prodReview"),
    path('blogReview', views.blogReview, name="blogReview"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('order_placed', views.orderDone, name="order_placed"),
    path('track_order', views.trackOrder, name='track_order'),

    path('cart/add/<int:id>', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cartDetail', views.cart_detail, name='cartDetail'),
    path('checkout', views.checkout, name='checkout'),
    path('placeOrder', views.place_order, name='placeOrder'),

    path('<str:slug>', views.postDetail, name="postDetail"),
    path('<str:type>/<str:slug>', views.DetailRecord, name="DetailRecord"),
    path('<str:type>/<str:slug>/delete', views.DeletebyUUID, name="Delete_with_diuu"),
    path('<str:type>/<str:slug>/update', views.UpdatebyUUID, name="Update_with_diuu"),
    path('error404', views.error404, name="error404"),

]
