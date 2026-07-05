from clothes import clothes
from grocery import grocery

c = clothes("clothes", "jeans", 100, 799, "balck", 'm')
g = grocery("grocery_section", "sugar", 60, 100, "sugarlite", "2026-06-01", "2027-06-01")

while True:
    print("Welcome to dmart\n1.Grocery section\n2.clothing_section\n3.exit\n")
    choice = int(input("enter yr choice !\n"))
    match choice:
        case 1:
            print(g.display_grocery_details())
        case 2:
            print(c.display_clothes_details())
        case 3:
            print("thank you !")
            break
        case _:
            print("invalid choice!")