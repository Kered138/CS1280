#Declaring Constant Car Speed
carSpeed = 70

#inputting and printing travel times and distances
travelTime1 = input("ENTER FIRST AMOUNT OF TIME TRAVELED >>> ")
distanceTraveled = int(travelTime1) * 70
print("You Traveled ", distanceTraveled, "Miles")

travelTime2 = input("ENTER SECOND AMOUNT OF TIME TRAVELED >>>")
distanceTraveled = int(travelTime2) * 70
print("You Traveled ", distanceTraveled, "Miles")

travelTime3 = input("ENTER THIRD AMOUNT OF TIME TRAVELED >>>")
distanceTraveled = int(travelTime3) * 70
print("You Traveled ", distanceTraveled, "Miles")

#Summing up all the times and distances to find the total distance
distanceTraveled = 0
distanceTraveled += int(travelTime1) * 70
distanceTraveled += int(travelTime2) * 70
distanceTraveled += int(travelTime3) * 70
print("Distance traveled in total is", distanceTraveled)


cTemp = input("INPUT CELSIUS TEMP >>> ")
fTemp = (9/5)*int(cTemp) + 32
print("The temperature in Fahrenheit is",fTemp)