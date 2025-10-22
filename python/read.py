fileName = input("Enter A File Name >>>")
file = open(fileName, "r")  
for line in  file:
    print(line.strip())
file.close()