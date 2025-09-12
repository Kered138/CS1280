weight = input("ENTER WEIGHT IN POUNDS >>>")
height = input("ENTER HEIGHT IN INCHES >>>")
bmi = (int(weight)/(int(height)**2))*703
print(f"Your bmi is {bmi:.2f}")

if bmi < 18:
    print("Underweight")
elif 18 <= bmi <= 24.99:
    print("Normal Weight")
elif 25 <= bmi <= 29.99:
    print("Overweight")
else:
    print("Obese")
