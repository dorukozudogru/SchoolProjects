#Parent class
class Product:
    #Constructor to initialize the attributes of the Product class
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    #Method to display the information of the product
    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)

#Child class that inherits from Product      
class Electronic(Product):
    #Constructor to initialize the attributes of the Electronic class, including those from the Product class
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    
    #Method to display the information of the electronic product, including the warranty
    def display_info(self):
        super().display_info()
        print("Warranty:", self.warranty)
        
#Child class that inherits from Product
class Grocery(Product):
    #Constructor to initialize the attributes of the Grocery class, including those from the Product class
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date
    
    #Method to display the information of the grocery product, including the expiration date
    def display_info(self):
        super().display_info()
        print("Expiration Date:", self.expiration_date)