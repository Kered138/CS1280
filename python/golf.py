import json
import os
def clear():
    os.system('cls')

clubs = {
    "1W"     : 0,
    "3W"     : 0,
    "5W"     : 0,
    "4I"     : 0,
    "6I"     : 0,
    "8I"     : 0,
    "PW"     : 0,
}

isPlaying = True

# clubs[input("enter club name >")] = int(input("enter distance"))
# distRem = int(input("ENTER YARDS REMAINING"))
# file = open('c:/Users/derek/CS1280/python/json/save.json','w+')
# data = {
#     "1W"     : 230,
#     "3W"     : 210,
#     "5W"     : 190,
#     "4I"     : 170,
#     "6I"     : 150,
#     "8I"     : 130,
#     "PW"     : 110,
# }

#json.dump(data, file)

scriptDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(scriptDir,"json","save.json")

def loadClubs():
    with open(filePath,"r") as f:
        my_dict = json.load(f)
    clubs = my_dict.copy()
    return clubs
def saveClubs():
    
    file = open(filePath,'w+')
    data = {
        "1W"     : int(input("Enter 1W Distance or 0 if no club >>>")),
        "2W"     : int(input("Enter 2W Distance or 0 if no club >>>")),
        "3W"     : int(input("Enter 3W Distance or 0 if no club >>>")),
        "4W"     : int(input("Enter 4W Distance or 0 if no club >>>")),
        "5W"     : int(input("Enter 5W Distance or 0 if no club >>>")),
        "3I"     : int(input("Enter 3I Distance or 0 if no club >>>")),
        "4I"     : int(input("Enter 4I Distance or 0 if no club >>>")),
        "5I"     : int(input("Enter 5I Distance or 0 if no club >>>")),
        "6I"     : int(input("Enter 6I Distance or 0 if no club >>>")),
        "7I"     : int(input("Enter 7I Distance or 0 if no club >>>")),
        "8I"     : int(input("Enter 8I Distance or 0 if no club >>>")),
        "9I"     : int(input("Enter 9I Distance or 0 if no club >>>")),
        "PW"     : int(input("Enter PW Distance or 0 if no club >>>")),
    }
    json.dump(data, file)
    global clubs
    clubs = data.copy()

def compare(clubs):
    global isPlaying
    dist = int(input("ENTER ESTIMATED DISTANCE TO HOLE OR 0 TO EXIT >>>"))
    if(dist == 0):
        isPlaying = False
    temp = 1000
    club = "putter"
    for key in clubs:
        #print(clubs[key])
        tmp = abs((clubs[key] - dist))
        if((tmp < temp) and tmp != 0):
            temp = tmp
            club = key
    return club
clear()
print("                ________        __   _____ ")
print("               /  _____/  ____ |  |_/ ____\\")
print("              /   \  ___ /  _ \|  |\   __\\ ")
print("              \    \_\  (  <_> )  |_|  |   ")
print("               \______  /\____/|____/__|   ")
print("                      \/                   ")
print("     '\                   .  .                        |>18>>  ")
print("       \              .         ' .                   |")
print("      O>>         .                 'o                |")
print("       \       .                                      |")
print("       /\    .                                        |")
print("      / /  .'                                         |")
print("   ^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
print("Hello! welcome to golf!")
print(f"{'-' * 30}")
choice = int(input("Would you like to (1) Save a new set of clubs or (2) Load existing clubs >>>"))
if(choice == 1):
    saveClubs()
else:
    clubs = loadClubs()
    

clear()

print("                   |H|")
print("                   |H|")
print("                   |||")
print("                   |||")
print("                   |V|")
print("                   | |")
print("     .----=--.-':'-; <")
print("    /=====  /'.'.'.'\\ |")
print("   |====== |.'.'.'.'.||             ___________")
print("    \=====  \\'.'.'.'/ /          .o8888888888888o.")
print("     '--=-=-='-:.:-'-`           88888888888888888")
print("                                 'Y8888888888888P`")
print("                                   `''''''''''''`")

print("Time to golf!")

while isPlaying:
    print()
    print("You Should Use your",compare(clubs))
    print()
clear()

print("Thank you for playing")






    
