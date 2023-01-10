from django.urls import path, include
from adminpannel import views
urlpatterns = [
        path('admin', views.adminHome, name="admin"),
        path('adminAmazonProducts', views.adminAmazonProducts, name="adminAmazonProducts"),
        path('admin_Q_Products', views.admin_Q_Products, name="admin_Q_Products"),
        path('adminPeopleSay', views.adminPeopleSay, name="adminPeopleSay"),
        path('adminblog', views.adminblog, name="adminblog"),
        path('orders', views.orders, name="orders"),
        path('view_Message/<int:id>', views.viewMessage, name="view_Message"),
        path('user_login', views.user_login, name="user_login"),
        path('user_logout', views.user_logout, name="user_logout"),
        path('Register', views.UserRegister, name="Register"),
        path('Delete/<int:id>/<str:type>', views.Delete, name="Delete"),
        path('MasterDelete/<str:type>', views.MasterDelete, name="MasterDelete"),
        path('Update/<int:id>/<str:type>', views.Update, name="Update"),
]
