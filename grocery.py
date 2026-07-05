from Dmart import Dmart


class grocery(Dmart):
    def __init__(self, category, product_name, qty, price, brand_name, mfg, exp):
        super().__init__(category, product_name, qty, price)
        self.brand_name = brand_name
        self.mfg = mfg
        self.exp = exp

    def display_grocery_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"brand_name:{self.brand_name}\nmfg :{self.mfg}\nexp:{self.exp}"


obj = grocery("grocery_section", "sugar", 60, 100, "sugarlite", "2026-06-01", "2027-06-01")
print(obj.display_grocery_details())