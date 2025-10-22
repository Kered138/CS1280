import csv 

def writeFile():
    filename = input("Enter a file name: ")
    file = open(filename, "a", newline="")

    writer = csv.writer(file)

    print("Enter new records to add to the CSV file.")
    print("Type 'done' as the name when you are finished. \n")

    while True:
        lname = input("Enter last name: ")
        if (lname.lower() == "done"):
            break
        fname = input("Enter first name: ")
        rank = input("Enter student rank: ")
        major = input("Enter major: ")
        gpa = input("Enter GPA: ")

        writer.writerow([lname,fname,rank,major,gpa])
        print("Record added. \n")

    print(f"New data successfully appended to {filename}")

    file.close()

def readFile():
    #fileName = ("python/studentFile.csv")
    fileName = input("Enter A File Name >>>")
    file = open(fileName, "r")  
    for line in  file:
        print(line.strip())
    file.close()
while True:
    choice = int(input("Would you like to (1)Read or (2)Append a File >>>"))

    match choice:
        case 1:
            readFile()
        case 2:
            writeFile()
        case _:
            print("error")