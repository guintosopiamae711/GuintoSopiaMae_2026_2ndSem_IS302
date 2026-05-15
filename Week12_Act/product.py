class Product:
    def __init__(self, product_id_smg, name_smg, price_smg, quantity_smg):
        self.__product_id_smg = product_id_smg
        self.__name_smg = name_smg
        self.__price_smg = price_smg
        self.__quantity_smg = quantity_smg

    def get_product_info(self):
        return f"{self.__product_id_smg},{self.__name_smg},{self.__price_smg},{self.__quantity_smg}"

    def get_id(self):
        return self.__product_id_smg

    def update_quantity(self, quantity_smg):
        self.__quantity_smg = quantity_smg

    def get_quantity(self):
        return self.__quantity_smg

    def __str__(self):
        return f"{self.__product_id_smg} {self.__name_smg} {self.__price_smg} {self.__quantity_smg}"
