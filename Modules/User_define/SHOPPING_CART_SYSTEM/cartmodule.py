

cart = []

def add_item(item):
    cart.append(item)

def remove_item(item):

    if item in cart:
        cart.remove(item)

def show_cart():
    return cart