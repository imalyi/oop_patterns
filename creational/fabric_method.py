from abc import ABCMeta, abstractmethod


class OrderProcessor:
    @abstractmethod
    def create_product(self):
        pass


class Product:
    @abstractmethod
    def process(self):
        pass


class ElectronicProduct(Product):
    def process(self):
        print(f"Processing {self}")

    def __str__(self):
        return "electronic product"


class ClothingProduct(Product):
    def process(self):
        print(f"Processing {self}")

    def __str__(self):
        return "clothing product"


class BookProduct(Product):
    def process(self):
        print(f"Processing {self}")

    def __str__(self):
        return "book product"


class ElectronicOrderProcessor(OrderProcessor):
    def create_product(self):
        return ElectronicProduct()


class ClothingOrderProcessor(OrderProcessor):
    def create_product(self):
        return ClothingProduct()


class BookOrderProcessor(OrderProcessor):
    def create_product(self):
        return BookProduct()


def create_and_process(factory: OrderProcessor):
    product = factory.create_product()
    product.process()


if __name__ == '__main__':
    book_factory = BookOrderProcessor()
    electronic_factory = ElectronicOrderProcessor()
    clothing_factory = ClothingOrderProcessor()

    create_and_process(book_factory)
    create_and_process(electronic_factory)
    create_and_process(clothing_factory)