def programPurpose():
    print("This program converts measurements \nin cups to fluid ounces. For your\n reference the formula is:")
    print("    1 cup = 8 fluid oucnes")

def requestCups():
    
    cups = int(input("Enter the number of cups: "))
    return cups

def performConversion(cups):
    #print("That converts to",(cups*8),"ounces.")
    return cups * 8

def main():
    programPurpose()
    cups = requestCups()
    oz = performConversion(cups)
    print(f"That converts to {oz} ounces.")

main()
