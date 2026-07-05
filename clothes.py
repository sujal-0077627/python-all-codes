from Dmart import dmart


class clothes(dmart):
    def __init__(self, category, product_name, qty, price, colour, size):
        super().__init__(category, product_name, qty, price)
        self.colour = colour
        self.size = size

    def display_clothes_details(self):
        super().display_store_details()
        return f"category: {self.category}\nproduct_name:{self.product_name}\nqty:{self.qty}\nprice:{self.price}"


obj = clothes("clothes", "jeans", 100, 799, "balck", 'm')
print(obj.display_clothes_details())