from django.shortcuts import render, redirect
from . models import Product, Order, CustomOrder
# Create your views here.



# admin : 
# username : admin
# password : 1234


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    if request.method == 'POST' and 'purchase' in request.POST:
        product_id_pur = request.POST.get('product_id_pur')
        if product_id_pur != 'Others':
            product = Product.objects.get(product_id = product_id_pur)
            customer_name = request.POST.get("customer_name")
            customer_email = request.POST.get('customer_email')
            quantity = request.POST.get('quantity')
            Order.objects.create(product_id=product, quantity=quantity, customer_name=customer_name, customer_email=customer_email)
            return redirect('/')
        else:
            customer_name = request.POST.get("customer_name")
            customer_email = request.POST.get('customer_email')
            quantity = request.POST.get('quantity')
            order_details = request.POST.get('custom_order')
            CustomOrder.objects.create(quantity=quantity, customer_name=customer_name, customer_email=customer_email, order_details=order_details)
            return redirect('/')
    if request.method == 'POST' and 'check' in request.POST:
        
        product_id_pur = request.POST.get('product_id_pur')
        if product_id_pur != 'Others':
            product = Product.objects.get(product_id = product_id_pur)
            context = {'products': products, 'description':product.product_description, 'price':product.product_price}
        
    return render(request, 'index.html', context)
