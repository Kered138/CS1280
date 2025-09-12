def primaryCheck(color):
    if (color == "red" or color == "R"):
        print("Color accepted")
        return True
    elif(color == "blue" or color == "B"):
        print("Color accepted")
        return True
    elif(color == "yellow" or color == "Y"):
        print("Color accepted")
        return True
    else:
        print("Color not primary", color)
        return False

def colorMix(c1 , c2):
    match c1:
        case "red":
            print("red")
            if(c2 == "blue"):
                return "purple"
            elif(c2 == "yellow"):
                return "orange"
            else:
                return "redder red"
        case "blue":
            print("blue")
            if(c2 == "red"):
                return "purple"
            elif(c2 == "yellow"):
                return "green"
            else:
                return "bluer blue"
        case "yellow":
            print("yellow")
            if(c2 == "blue"):
                return "green"
            elif(c2 == "red"):
                return "orange"
            else:
                return "yellower yellow"
        
color1 = input("PICK A PRIMARY COLOR >>>")
color2 = input("PICK A PRIMARY COLOR >>>")

print(primaryCheck(color1))
print(primaryCheck(color2))
print( "Mixed Color Is > "+colorMix(color1,color2)+" <")



