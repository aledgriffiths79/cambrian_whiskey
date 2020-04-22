from django.shortcuts import render, redirect, reverse

# Create your views here.

# view_cart renders everything within the cart
def view_cart(request):
  """ A view that renders the cart contents page"""
  return render(request, 'cart.html')

# line 13 quantity=int(request.POST.get('quantity')) i had an error when pressing the amend button from cart.html. What i did was i had capital Q for quantity in the form with tag label attribute name value, Quantity instead of quantity in the cart.html file. So  Yessir! Exaclty! It's the request getting the post method of the name="" attribute from your form for the name="quantity" field.
def add_to_cart(request, id):
  """Add a quantity of the specified product to the cart. Gets the int(integer) from the form in the products.html file"""
  quantity=int(request.POST.get('quantity'))

  cart = request.session.get('cart', {})
  if id in cart:
    cart[id] = int(cart[id] + quantity)
  else:
    cart[id] = cart.get(id, quantity)

  request.session['cart'] = cart
  return redirect(reverse('index'))


def adjust_cart(request, id):
  """Adjust the quantity of the specified product by the specified amount"""
  quantity = int(request.POST.get('quantity'))
  cart = request.session.get('cart', {})

  if quantity > 0:
    cart[id] = quantity
  else:
    cart.pop(id)

  request.session['cart'] = cart
  return redirect(reverse('view_cart'))

