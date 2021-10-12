'''
3. As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).
    a. As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.
    b. As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)
    c. As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

'''

class ShoppingCart:
    def __init__(self):
        self.price_total_cart = ""
        self.product_list = []
        self.product_price_list = []
    
    def calculate_total(self):
        self.price_total_cart = sum(self.product_price_list)
        return self.price_total_cart

    def add_to_cart (self, product):
        self.product_list = self.product_list.append(product)
        return self.product_list

    def empty_cart (self):
        self.product_list = self.product_list.clear()
        return self.product_list

