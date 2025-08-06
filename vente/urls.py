from django.urls import path

from vente.controllers.UserController import login_user, login_user_page

urlpatterns = [
    path('login_page/', login_user_page, name='login_user_page'),
    path('login/', login_user, name='login_user'),
]