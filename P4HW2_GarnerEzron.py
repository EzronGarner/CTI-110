# Ezron Garner
#10/30/26
# P4HW2
# salary caluclator

#request employee infor
name = input("Enter employee's name or 'done' to finish: ")

#Create accumulator variables for overtime pay, regular pay, gross pay and hours worked

overtimepay_total=0
regularpay_total=0
grosspay_total=0
employee_count=0

while name != 'done':
    #Add emplyee count plus one
    employee_count += 1
    #ask for employee information
    hours=float(input("How many hours did " +name + " work this week?"))
    rate=float(input("What is " +name + "'s hourly pay rate?"))
        #Evaluate Overtime
    if hours > 40:
        #calculate overtime
        overtime_hours = hours - 40
        #calculate overpay
        overtime_pay = overtime_hours * (rate * 1.5)
        # caulcuate salary for regular hours
        gross_pay = regular_pay + overtime_pay
    else:
            overtime_pay = 0
            Overtime_hours = 0
            regular_pay = hours * rate
            gross_pay = regular_pay

            #add to accumulator totals
            overtimepay_total += overtime_pay
            regularpay_total += regular_pay
            grosspay_total += gross_pay
            #Display results
    print("---------------")
    print("Employee Name: ", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<12}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("---------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<12}{regular_pay:<15}{gross_pay:<12}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of emplyees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total,',.2f'))
print("Total amount paid for regular pay: $", format(regularpay_total,',.2f'))
print("Total amount paid for gross pay: $", format(grosspay_total,',.2f'))