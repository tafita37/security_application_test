# views.py
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
        print("trouvé")
    except ObjectDoesNotExist:
        user = None
        print("introuvable")
    return redirect("login_user_page")