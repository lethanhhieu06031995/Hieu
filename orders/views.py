from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import EmailMessage

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		chuoi_don_hang='<table width="100%">'
		if form.is_valid():
			order = form.save()
			chuoi_don_hang+='<tr><td colspan="3">Đơn hàng của bạn # ' + str(order.id) + '</td></tr>'
			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
				)
				chuoi_don_hang+='<tr><td rowspan="4"><img src="http://127.0.0.1:8000'+item['product'].hinh_san_pham.url+'" width="250px"></td>'
				chuoi_don_hang+='<td>Sản phẩm</td><td>'+item['product'].ten_san_pham+'</td></tr>'
				chuoi_don_hang+='<tr><td>Tên shop</td><td>Trung tâm tin học</td></tr>'
				chuoi_don_hang+='<tr><td>Thanh toán</td><td>'+str(item['price']*item['quantity'])+'</td></tr>'
				chuoi_don_hang+='<tr><td>Người nhận</td><td>'+order.last_name +' ' + order.first_name +' '+order.postal_code 
				chuoi_don_hang+= '<br/>'+order.address+'</td></tr>'

			cart.clear()
			chuoi_don_hang+='</table>'
			email = EmailMessage('Xác nhận đơn hàng', chuoi_don_hang, to=[order.email]) 
			email.content_subtype = "html"
			print(email.send())
		return render(request, 'orders/order/created.html', {'order': chuoi_don_hang})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'form': form})