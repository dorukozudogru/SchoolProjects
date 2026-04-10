import pickle

class Product:
    def __init__(self, name, price, expiry_date, is_dairy):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date
        self.is_dairy = is_dairy
        
product1 = Product("Milk", 2.5, "2026-02-01", True)
product2 = Product("Bread", 1.5, "2026-02-15", False)
product3 = Product("Cheese", 3.0, "2026-01-10", True)

# Record products
products = [product1, product2, product3]
key = 1024

# file = open("products.dat", "wb")
with open("/Users/dorukozudogru/Projects/IPS/G12/For Lesson - Ch. 23/products.dat", "wb") as file:
    for product in products:
        hashed_name = hash(product.name)
        file.seek(hashed_name % key)
        pickle.dump(product, file)
        
search_value = input("Enter product name to search: ")       

# file = open("products.dat", "rb")
with open("/Users/dorukozudogru/Projects/IPS/G12/For Lesson - Ch. 23/products.dat", "rb") as file:
    file.seek(hash(search_value) % key)
    found_product = pickle.load(file)
    print(f"Product Name: {found_product.name}")
    print(f"Price: {found_product.price}")
    print(f"Expiry Date: {found_product.expiry_date}")
    print(f"Is Dairy: {found_product.is_dairy}")