from django.urls import path, include
from dronzaPanel import views
urlpatterns = [
        path('admin', views.adminHome, name="admin"),
        path('adminHomeSlider', views.adminHomeSlider, name="adminHomeSlider"),
        path('adminHowItWork', views.adminHowItWork, name="adminHowItWork"),
        path('adminHowToUse', views.adminHowToUse, name="adminHowToUse"),
        path('adminHomeAbout', views.adminHomeAbout, name="adminHomeAbout"),
        path('adminDroneProducts', views.adminDroneProducts, name="adminDroneProducts"),
        path('adminHomeSRFP', views.adminHomeSRFP, name="adminHomeSRFP"),
        path('adminVideoGallery', views.adminVideoGallery, name="adminVideoGallery"),
        path('adminPeopleSay', views.adminPeopleSay, name="adminPeopleSay"),
        path('adminOurPartner', views.adminOurPartner, name="adminOurPartner"),
        path('adminabout', views.adminaboutTitlePost, name="adminabout"),
        path('adminqualityTrust', views.adminQualityTrust, name="adminqualityTrust"),
        path('adminTeam', views.adminOurTeam, name="adminTeam"),
        path('adminservicesType', views.adminServicesType, name="adminservicesType"),
        path('adminpricing', views.adminPricing, name="adminpricing"),
        path('admingallery', views.adminGallery, name="admingallery"),
        path('adminsocialmedia', views.adminsocial_media, name="adminsocialmedia"),
        path('adminblog', views.adminuser_blog, name="adminblog"),
        path('orders', views.orders, name="orders"),
        path('adminuser_logout', views.user_logout, name="adminuser_logout"),
        path('adminRegister', views.UserRegister, name="adminRegister"),
        path('adminview_Message/<int:id>', views.viewMessage, name="adminview_Message"),
        path('user_login', views.user_login, name="user_login"),
        path('user_logout', views.user_logout, name="user_logout"),
        path('Register', views.UserRegister, name="Register"),
        path('UserList', views.user_list, name="UserList"),
        path('view_Message/<int:id>', views.viewMSG, name="view_Message"),
        path('Delete/<int:id>/<str:type>', views.Delete, name="Delete"),
        path('MasterDelete/<str:type>', views.MasterDelete, name="MasterDelete"),
        path('Update/<int:id>/<str:type>', views.Update, name="Update"),
]
