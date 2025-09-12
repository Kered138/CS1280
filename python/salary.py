salary = int(input("ENTER YEARLY SALARY >>>"))
yearsOnJob = int(input("ENTER THE NUMBER OF YEARS OF EMPLOYMENT >>>"))

if(salary >= 30000 & yearsOnJob >= 2):
    if(yearsOnJob >= 2):
        print("you qualify")
    else:
        print("you havent worked long enough to qualify")
else:
    print("You dont make enough money")

