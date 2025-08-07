# views.py
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from vente.model.Product import Product

@require_GET
def load_product_list(request):
    if 'user_id' not in request.session:
        return redirect("login_user_page")
    products=Product.objects.all()
    return render(request, "views/products.html", {"products": products})

@require_GET
def load_product_detail(request):
    if 'user_id' not in request.session:
        return redirect("login_user_page")
    product_id = request.GET.get("produt_id")
    product = Product.objects.get(id=product_id)
    return render(request, "views/product_detail.html", {"product": product})