# Ezron Garner
#10/3/26
# P3HW2
# salary caluclator

#request employee infor
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
federal_tax_rate = float(input("Enter federal tax withholding rate (as a decimal): "))

# Evaluate overtime
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

#Display results
print("---------------")
print("Employee Name: ", name)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<12}{"Regular Pay":<15}{"Gross Pay":<12}')
print("---------------------")
print(f'{hours:<15}{rate:<12}{overtime_pay:<12}{regular_pay:<15}{gross_pay:<12}')
