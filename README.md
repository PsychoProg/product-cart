 ```
# Django shopping cart 

This is a Django e-commerce website that allows users to browse products and courses, add items to their cart, and checkout.

## Getting Started

To get started, clone the repository and install the dependencies.

```
git clone https://github.com/PsychoProg/product-cart.git

cd product-cart
pip install -r requirements.txt

```

Now, you need to create a database and apply the migrations.

```

python manage.py migrate

```

Finally, you can start the development server.

```

python manage.py runserver

```

## Usage

To use the website, first create a user account. Then, you can browse the products and courses and add items to your cart. When you're ready to checkout, click the "Checkout" button. You'll be prompted to enter your payment information and shipping address. Once you've submitted your order, you'll receive a confirmation email.

## Code Explanation

The `models.py` file defines the following models:

* `Product`: This model represents a product that can be added to the cart.
* `Course`: This model represents a course that can be added to the cart.
* `Order`: This model represents an order that has been placed.
* `OrderItem`: This model represents an item in an order.
