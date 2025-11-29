from products import Product


class Store:

    def __init__(self, products: list[Product]):
        self._products = list(products)

    def add_product(self,product):
        """Fügt ein Produkt zum Store hinzu."""
        self._products.append(product)

    def list_products(self):
        for product in self._products:
            product.show()

    def remove_product(self, product):
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        total_items = 0
        for product in self._products:
            total_items += product.quantity
        return total_items

    def get_all_products(self) -> list[Product]:
        active_product = []
        for product in self._products:
            if product.is_active():
                active_product.append(product)
        return active_product

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, amount in shopping_list:
            product.buy(amount)
            total_price += product.price * amount
        return total_price