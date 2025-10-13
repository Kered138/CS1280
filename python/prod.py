import random
products = [
    ("Potato Chips",7.49,0.01),
    ("Bananas",0.59,0.01),
    ("Milk",2.49,0.01),
    ("Bread",1.99,0.01),
    ("Eggs",3.49,0.01),
    ("6-pack Spring Water",2.49,0.02),
    ("4-pack Breakfast Sandwiches",7.99,0.03),
    ("Frozen Green Beans",1.99,0.01),
    ("12-count Coffe Pods",7.99,0.03),
    ("64-oz Laundry Detergent",5.99,0.02)]

products.append(("Frozen Corn",1,99,0.01))
print(products)
products.remove(("Bananas",0.59,0.01))
# products.remove(products[1])
print(products[0])
del products[0]
print(random.randint(1,10))