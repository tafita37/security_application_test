from django.urls import path

from vente.controllers.ProductController import load_product_detail, load_product_list, post_comment
from vente.controllers.UserController import login_user, login_user_page

urlpatterns = [
    path('login_page/', login_user_page, name='login_user_page'),
    path('login/', login_user, name='login_user'),
    path('products/', load_product_list, name='list_products'),
    path('detail_product/', load_product_detail, name='detail_product'),
    path('post_comment/', post_comment, name='post_comment'),
]