import os
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_user_menu():
    print("Menu Choices:\n 1 - Add an Item \n 2 - Remove an Item \n 3 - View Cart \n 4 - View Cart Value \n 5 - Exit")
    return int(input("Enter A Menu Choice >>>"))



def add_item():
    print("add Item")
    clear()
    print("List of Items")
    for i in  range(0,len(products)):
        print(f"{i + 1} {products[i]}")
    return int(input("Enter Item you wish to buy"))
def remove_item():
    print("Remove Item")
def view_cart():
    print("viewCart")
def display_cart_value():
    print("displayCart Value")
def shopping_cart_program(products):
    shoppingCart = []
    while True:
        choice = display_user_menu()
        match choice:
            case 1:
                add_item()
            case 2:
                remove_item()
            case 3:
                view_cart()
            case 4:
                display_cart_value()
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