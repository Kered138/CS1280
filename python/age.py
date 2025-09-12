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