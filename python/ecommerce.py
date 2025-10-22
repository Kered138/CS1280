import os
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_user_menu():
    print("Menu Choices:\n 1 - Add an Item \n 2 - Remove an Item \n 3 - View Cart \n 4 - View Cart Value \n 5 - Exit")
    return int(input("Enter A Menu Choice >>>"))

def display_products(products):
    print("\nList of Products")
    index = 1
    for product in products:
        productName, productPrice, discountPercent = product
        if discountPercent > 0:
            print(f"{index}. {productName} - ${productPrice:.2f} ({int(discountPercent*100)}% off)")
        else:
            print(f"{index}. {productName} - ${productPrice:.2f}")
        index = index + 1



def add_item(products, cart):
    clear()
    display_products(products)
    productNum = int(input("Select a product by number: "))
    quantity = int(input("Enter quantity: "))
    index = 1
    for product in products:
        if index == productNum:
            productName, productPrice, discountPercent = product
            cart.append((productName, productPrice, discountPercent, quantity))
        index = index + 1

def remove_item(cart):
    clear()
    print("\nItems in your cart:")
    index = 1
    for item in cart:
        print(f"{index}. {item[3]} x {item[0]}")
        index = index + 1

    remove_num = int(input("Enter the number of the item to remove: "))

    index = 1
    for item in cart:
        if index == remove_num:
            cart.remove(item)
            break
        index = index + 1
    
def view_cart(cart):
    clear()
    print("\nYour Shopping Cart:")
    index = 1
    for item in cart:
        productName, productPrice, discountPercent, quantity = item
        discountedPrice = productPrice * (1 - discountPercent)
        if discountPercent > 0:
            print(f"{index}. {quantity} x {productName} "
                  f"@ ${discountedPrice:.2f} each "
                  f"(after {int(discountPercent*100)}% off)")
        else:
            print(f"{index}. {quantity} x {productName} @ ${productPrice:.2f}")
        index += 1
def display_cart_value(cart):
    clear()
    totalCost = 0
    for item in cart:
        productName, productPrice, discountPercent, quantity = item
        discounted_price = productPrice * (1 - discountPercent)
        totalCost = totalCost + discounted_price * quantity
    print(f"The total value of your cart is ${totalCost:.2f}")
def shopping_cart_program(products):
    shoppingCart = []
    while True:
        choice = display_user_menu()
        match choice:
            case 1:
                add_item(products,shoppingCart)
            case 2:
                remove_item(shoppingCart)
            case 3:
                view_cart(shoppingCart)
            case 4:
                display_cart_value(shoppingCart)
            case _:
                print("exit")
                sys.exit()

products = [
    ("Potato Chips",7.49,0.01),
    ("Bananas",0.59,0.01),
    ("Milk",2.49,0.01),
    ("Bread",1.99,0.01),
    ("Eggs",3.49,0.01),
    ("6-pack Spring Water",2.49,0.02),
    ("4-pack Breakfast Sandwiches",7.99,0.03),
    ("Frozen Green Beans",1.99,0.01),
    ("12-count Coffee Pods",7.99,0.03),
    ("64-oz Laundry Detergent",5.99,0.02)] 

# for i in  range(0,len(products)):
#     print(products[i])
clear()
shopping_cart_program(products)