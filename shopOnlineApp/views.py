from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    prolist = Product.objects.order_by('name')
    context = {
        'products': prolist,
    }
    return render(request, 'shopOnlineApp/trangchu.html', context)


def product_detail(request, id=None):
    product_detail = Product.objects.get(pk=id)
    cart = CartAddProductForm()
    context = {
        'product_details': product_detail,
        'cart': cart,
    }
    return render(request, 'shopOnlineApp/product_detail.html', context)


def chi_tiet(request, id):
    sanpham = Tivi.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    context = {
        'sanpham': sanpham,
        'cart_product_form': cart_product_form,
    }
    return render(reequest, 'Tivi_app/chi_tiet_san_pham.html', context)
