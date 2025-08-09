# views.py
from django.db import connection
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from vente.model.Users import Users

@require_GET
def login_user_page(request):
    return render(request, "views/login_user.html")

@require_POST
def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = Users.objects.get(email=email, password=password)
        request.session['user_id'] = user.id
        return redirect("list_products")
    except ObjectDoesNotExist:
        user = None
        return redirect("login_user_page")
    
# @require_POST
# def login_user(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
    
#     # Version vulnérable utilisant une requête brute
#     with connection.cursor() as cursor:
#         cursor.execute(f"SELECT * FROM users_users WHERE email = '{email}' AND password = '{password}'")
#         row = cursor.fetchone()
    
#     if row:
#         # Création de la session si l'utilisateur existe
#         user = Users.objects.get(id=row[0])  # On récupère l'objet User normalement
#         request.session['user_id'] = user.id
#         return redirect("list_products")
    
#     return redirect("login_user_page")