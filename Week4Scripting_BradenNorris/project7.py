startSalary = int(input("Please enter beginning salary: "))
percentIncrease = (float(input("Please enter percentage increase: ")) / 100)
numberYears = int(input("Please enter number of years in schedule: "))
for i in range(1,numberYears):
    print("Year: ", i, ", Salary: ", "{:.2f}".format(startSalary*((1+percentIncrease)**(i-1))))
