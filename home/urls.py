from django.urls import path, include
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

    path('shopDetail/<int:id>/<str:uuid>/<str:type>', views.shopDetail, name="shopDetail"),
    path('postDetail/<int:sNo>', views.postDetail, name="postDetail"),
    path('DetailRecord/<int:id>/<str:type>', views.DetailRecord, name="DetailRecord"),
    path('Detail_with_diuu/<int:id>/<str:uuid>/<str:type>', views.RecordbyUUID, name="Detail_with_diuu"),
    path('Delete_with_diuu/<str:uuid>/<str:type>', views.DeletebyUUID, name="Delete_with_diuu"),
    path('Update_with_diuu/<str:uuid>/<str:type>', views.UpdatebyUUID, name="Update_with_diuu"),
    path('error404', views.error404, name="error404"),


    path('testing', views.testing, name="testing"),
]