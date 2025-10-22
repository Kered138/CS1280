import csv
filename = input("Enter a file name: ")
file = open(filename, "a", newline="")
write = csv.writer(file)
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
    write.writerow([lname,fname,rank,major,gpa])
    print("Record added. \n")
print(f"New data successfully appended to {filename}")
file.close()