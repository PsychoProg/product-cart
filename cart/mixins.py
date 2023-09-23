# mixins.py
from cart.cart import Cart

class CartMixin:
    def get_cart(self):
        cart = Cart(self.request)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.get_cart()
        return context