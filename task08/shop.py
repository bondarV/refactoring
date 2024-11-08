
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")
        print(f"Number of Units: {self.number_of_units}")

    def open_shop(self):
        print("The online shop is open")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        return self.discount_products

    def add_discount_product(self, product):
        self.discount_products.append(product)
