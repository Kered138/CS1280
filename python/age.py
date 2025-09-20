
anotherAge = "y"
while anotherAge == "y":
    age = int(input("ENTER YOUR AGE >>>"))
    if(age < 1):
        print("infant")
    elif(age < 5):
        print("toddler")
    elif(age < 13):
        print("child")
    elif(age < 18):
        print("teen")
    elif(age < 65):
        print("adult")
    else:
        print("senior")
    anotherAge = input("want to add another age y or n >>>" )

for i in range(10):
    print(i)
while i != 20:
    i += 1
    print(i)

num1 = 1
num2 = 2
tempNum = 0

print(num1)
print(num2)

def nextFibNum():
    global num1
    global num2
    tempNum = num2
    num2 = num1 + num2
    num1 = tempNum
    print(num2)

def nextPowerofTwo():
    global num1
   
    num1 = num1 * 2
    print(num1)
for i in range(100):
    nextPowerofTwo()