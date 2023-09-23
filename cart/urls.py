# urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('clear/', views.ClearCartView.as_view(), name='clear_cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
]