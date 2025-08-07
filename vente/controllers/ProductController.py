# views.py
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST
from vente.model.Product import Product
from vente.model.Comment import Comment
from vente.model.Users import Users

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
    comments= Comment.objects.filter(product=request.GET.get("product_id")).order_by('-created_at')
    user_id = request.session.get("user_id")
    product_id = request.GET.get("product_id")
    product = Product.objects.get(id=product_id)
    return render(request, "views/product_detail.html", {"product": product, "user_id": user_id, "comments": comments})

@require_POST
def post_comment(request) :
    if 'user_id' not in request.session:
        return redirect("login_user_page")
    user_id = request.session.get("user_id")
    product_id = request.POST.get("product_id")
    content = request.POST.get("content")
    
    if not content:
        return redirect(f"product_detail?produt_id={product_id}")
    
    comment = Comment(user=Users(user_id), product=Product(product_id), content=content)
    comment.save()
    
    return HttpResponseRedirect(f"/vente/detail_product/?product_id={product_id}")