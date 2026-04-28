# secure_inventory.py

class Product:
    def __init__(self, name_smg, price_smg, quantity_smg):
        self.__name_smg = name_smg          # private attribute
        self.__price_smg = price_smg
        self.__quantity_smg = quantity_smg

    # method to display product information
    def get_product_info_smg(self):
        print("Product:", self.__name_smg)
        print("Price:", self.__price_smg)
        print("Quantity:", self.__quantity_smg)

    # method to update quantity
    def update_quantity_smg(self, quantity_smg):
        if quantity_smg >= 0:
            self.__quantity_smg = quantity_smg
        else:
            print("Invalid quantity")

    # method to update price
    def update_price_smg(self, price_smg):
        if price_smg > 0:
            self.__price_smg = price_smg
        else:
            print("Invalid price")


# create a product object
product1_smg = Product("Laptop", 45000, 10)

# display product info
product1_smg.get_product_info_smg()