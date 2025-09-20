import datetime 

val = "Geeks"
print(f"{val}for{val} is a portal for {val}.")


name = "Om"
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")

firstName = input("ENTER FIRST NAME >>>")
lastName = input("ENTER LAST NAME >>>")
weight = float(input("ENTER WEIGHT IN POUNDS >>>"))
bmi = float(input("ENTER BMI >>>"))

print()
print(f"Last Name is {lastName} and the First Name is {firstName}")
print(f"{firstName}'s weight is {weight}")
print(f"{firstName}'s BMI is {bmi:.2f}")

today = datetime.datetime.today()
print(f"{today: %B %d, %Y}")