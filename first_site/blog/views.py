from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from blog.forms import ProductForm,RegisterForms
from blog.models import Product,Cart
from first_site.inner.helper import helper_add_to_cart,helper_delete_to_cart

# Create your views here.
def registered_user(request):
    form=RegisterForms()
    if request.method=='POST':
        userName = request.POST.get('username', None)
        userPass = request.POST.get('password', None)
        user = User.objects.create_user(userName, userPass)
        user.save()
    return render(request,'register.html', {'form': form})

    
def create_product(request): 
    product = ProductForm()
    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
    return render(request,'create_product.html', {'form': product})
    
def list_all_products(request):
    if request.method  == 'GET':
        product = Product.objects.all()
    return render(request,'list_all_product.html', {'product': product})    



# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         cart_session = request.session.get('cart', [])
#         cart_items = {'Name': product.name, 'price':product.price,'quality':product.quality}
#         cart_session.append(cart_items)
#         request.session['cart'] = cart_session
#         print(request.session['cart'])
#     return render(request,'add_to_cart.html')
def add_to_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        cart = helper_add_to_cart(request,id)
    return render(request,'add_to_cart.html',{'cart':cart})
        




def delete_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        
        cart_delete = helper_delete_to_cart(request,id)
        print(cart_delete)
    
    return render(request,'add_to_cart.html')



