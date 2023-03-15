from blog.models import Product
def helper_add_to_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        product=Product.objects.get(id=id)
        cart_session = request.session.get('cart', [])
        cart_items = {'Name': product.name, 'price':product.price,'quality':product.quality}
        cart_session.append(cart_items)
        request.session['cart'] = cart_session
        print(request.session['cart'])
    return render(request,'add_to_cart.html')

def helper_delete_to_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        cart = Cart.objects.get(id=id)
        cart.delete()
    cart = Cart.objects.all()
    return render(request,'add_to_cart.html', {'cart': cart})



