from wild_zoo.project import Product


class ProductRepository:
    def __init__(self, products = []):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for item in self.products:
            if item.name == product_name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if item.name == product_name:
                self.products.remove(item)

    def __repr__(self):
        result = []
        for item in self.products:
            k, v = item.__dict__
            result.append(f'{item.__dict__[k]}: {item.__dict__[v]}')

        return '\n'.join(result)

