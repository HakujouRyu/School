hoursWorked = int(input("Please enter the number of hours worked: "))
payRate = 10
otRate = 15
overTime = (hoursWorked - 40)
grossPay = ((hoursWorked - overTime) * payRate)

if overTime > 0:
    grossPay = ((hoursWorked - overTime) * payRate) + (overTime * otRate)


print(grossPay)
