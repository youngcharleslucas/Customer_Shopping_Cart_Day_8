'''
Customer Shopping Cart Lab

        As a developer, I want to use Python’s proper snake_case for variable names.

        As a developer, I want to create a Customer, ShoppingCart, and Product class.

2. As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.
    a. As a developer, I want the Product class’s initializer to take in the initial values for the name, price, and category via parameters

3. As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).
    a. As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.
    b. As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)
    c. As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

4. As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. 
        (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into 
        the customer.py file)
    a.  As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.
    b.  As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will 
        call the shopping cart’s add product method)
    c.  As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s 
        products list and print each product to the terminal)

As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact 
with the object’s methods:

1. Print the customer’s name to the terminal

2. Call the customer’s add product to shopping cart method three times and add the three products objects you created

3. Call the customer’s view products method

4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal

5. Call the customer’s shopping cart’s empty cart method

6. Check if all products have been removed from the shopping cart

Files:

customer.py

shopping_cart.py

Product.py

#-------------------------




'''
from shopping_cart import ShoppingCart
from customer import Customer

from Product import Product

#1.-------------------------------------

def print_name():
    customers_name = Customer
    print(customers_name.customers_name())

print_name()

#2.------------------------------------------

def add_item_cart (product):
    item_added = Customer
    return item_added.customer_add_cart(product)

add_item_cart()
add_item_cart()
add_item_cart()

#3.------------------------------------------

def view_product():
    products = Customer
    print(products.customer_view_cart())

view_product()

#4-------------------------------------------

def view_price_total():
    view_total_price = ShoppingCart
    print(f'Your total is {view_total_price.calculate_total()}')

view_price_total()

#5----------------------------------------------

def empty_cart():
    empty_shopping_cart = ShoppingCart
    empty_shopping_cart.empty_cart()

empty_cart()

#6----------------------------------------------


products_in_cart = view_product()
print(products_in_cart)