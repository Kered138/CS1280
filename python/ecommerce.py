#Shopping cart function - list addable and removable, readable
#cost function, show cost of items, discount
#list of items avaible for sale, and there prices,discounts
class item:
    def __init__(self, name, price,desc):
        self.name = name
        self.price = price
        self.desc = desc
broom = item("Broom",9.99,"Modern Versitile Broom for Cleaning Everywhere")
def Menu():
    print("WELCOME TO SAHARA")
    print("Where would you like to go, (1) View Products, (2) View Cart, (3) Checkout")
    choice = int(input("CHOOSE >>>")) 
            
print(broom.name)
print(broom.price)