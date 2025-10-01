import os
import time
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayUserMenu():
    print("Menu Choices:\n 1 - Add an Item \n 2 - Remove an Item \n 3 - View Cart \n 4 - View Cart Value \n 5 - Exit")
    return int(input("Enter A Menu Choice >>>"))
def addItem():
    pass
def removeItem():
    pass
def viewCart():
    pass
def displayCartValue():
    pass
def shoppingCartProgram(products):
    shoppingCart = []
    while True:
        choice = displayUserMenu()
        match choice:
            case 1:
                addItem()
            case 2:
                removeItem()
            case 3:
                viewCart()
            case 4:
                displayCartValue()
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
    ("12-count Coffe Pods",7.99,0.03),
    ("64-oz Laundry Detergent",5.99,0.02)]
