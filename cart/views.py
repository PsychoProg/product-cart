# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CartMixin
from .models import Course, Product, Order, OrderItem


class ProductListView(CartMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(CartMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class CourseListView(CartMixin, ListView):
    model = Course
    template_name = 'courses/course_list.html'


class CourseDetailView(CartMixin, DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


class CartView(CartMixin, TemplateView):
    template_name = 'cart/cart.html'


class AddToCartView(LoginRequiredMixin, CartMixin, TemplateView):
    template_name = 'cart/add_to_cart.html'

    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        product_id = request.POST.get('product_id')
        product_type = request.POST.get('product_type')
        if product_type == 'product':
            product = get_object_or_404(Product, id=product_id)
        elif product_type == 'course':
            product = get_object_or_404(Course, id=product_id)
        else:
            return redirect('home')
        cart.add(product=product, product_type=product_type)
        return redirect('cart:cart')


class RemoveFromCartView(LoginRequiredMixin, CartMixin, TemplateView):
    template_name = 'cart/remove_from_cart.html'

    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        unique_id = request.POST.get('unique_id')
        cart.remove(unique_id)
        return redirect('cart:cart')


class ClearCartView(LoginRequiredMixin, CartMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        cart.clear()
        return redirect('cart:cart')


class CheckoutView(LoginRequiredMixin, CartMixin, TemplateView):
    template_name = 'cart/checkout.html'

    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        order = Order.objects.create(user=request.user)
        for item in cart:
            product_type = item['product_type']
            product_id = item['product_id']
            if product_type == 'product':
                product = get_object_or_404(Product, id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    course=None,
                    product_type=product_type,
                    price=item['price'],
                )
            elif product_type == 'course':
                course = get_object_or_404(Course, id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=None,
                    course=course,
                    product_type=product_type,
                    price=item['price'],
                )
            else:
                continue
            
        cart.clear()
        # return redirect('cart:order_detail', order_id=order.id)
        return redirect('cart:order_detail', pk=order.pk)

class OrderDetailView(LoginRequiredMixin, CartMixin, DetailView):
    model = Order
    template_name = 'cart/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset