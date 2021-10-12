'''
4. As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. 
        (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into 
        the customer.py file)
    a.  As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.
    b.  As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will 
        call the shopping cart’s add product method)
    c.  As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s 
        products list and print each product to the terminal)
'''

from shopping_cart import ShoppingCart

class Customer:
    def __init__(self):
        self.customer_name = ""
        self.customer_cart = ""

    def customers_name (self):
        self.customer_name = input("Enter your first and last name: ")
        return self.customer_name

    def customer_add_cart (self, product):
        add_product = ShoppingCart()
        return add_product.add_to_cart(product)
        
    def customer_view_cart(self):
        customer_cart = ShoppingCart()
        print_customer_cart = customer_cart.product_list
        for item in print_customer_cart:
            print(item)


