import os
def clear():
    os.system('cls')


lbs = float(input("ENTER PACKAGE WEIGHT IN POUNDS >>>"))
rate = 0.0
if (lbs <= 2.0):
    rate = 1.50
elif (lbs <= 6.0):
    rate = 3.00
elif (lbs <= 10.0):
    rate = 4.0
else:
    rate = 4.75
total = rate * lbs

clear()

print(f"{'=' * 30}\n       SHIPPING RECEIPT \n{'=' * 30}")
print(f"Package Weight:         {lbs:.2f} lbs")
print(f"Rate per Pound:     $   {rate:.2f}")
print(f"Total Cost:         $   {total:.2f}")
print(f"{'=' * 30}\n   Thank you for your order!  \n{'=' * 30}")