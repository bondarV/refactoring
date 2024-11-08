
from shop import Shop, Discount

if __name__ == '__main__':
    store = Shop("Tech Haven", "Electronics")

    print(store.shop_name)
    print(store.store_type)

    store.describe_shop()
    store.open_shop()

    store1 = Shop("Book Nook", "Books")
    store2 = Shop("Fashion Fiesta", "Clothing")
    store3 = Shop("Gadget Galaxy", "Electronics")

    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()

    store = Shop("Tech Haven", "Electronics")
    print(store.number_of_units)
    store.number_of_units = 50
    print(store.number_of_units)

    store.set_number_of_units(100)
    print(store.number_of_units)
    store.increment_number_of_units(25)
    print(store.number_of_units)

    store_discount = Discount("Discount Mart", "General")
    store_discount.add_discount_product("Laptop")
    store_discount.add_discount_product("Smartphone")
    print(store_discount.get_discount_products())
