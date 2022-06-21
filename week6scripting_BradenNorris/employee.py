import data as data

fileName = input("enter the file name: ")

inputFile = open(fileName, 'r')

print("Name, Hours, Total Pay")

for line in inputFile:
    employeeList = line.split()
    name = employeeList[0]
    hours = int(employeeList[1])
    payRate = float(employeeList[2])
    totalPayRate = hours * payRate
    print(name, hours, totalPayRate)
