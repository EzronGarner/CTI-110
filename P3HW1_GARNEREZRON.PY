#Ezron Garner
#10/3/26
#P3HW1
# This program takes a number grade and determines the average and displays a letter grade based on the average.

#Enter grades for six modules

mod_1 = float(input("Enter the grade for module 1: "))
mod_2 = float(input("Enter the grade for module 2: "))
mod_3 = float(input("Enter the grade for module 3: "))
mod_4 = float(input("Enter the grade for module 4: "))
mod_5 = float(input("Enter the grade for module 5: "))
mod_6 = float(input("Enter the grade for module 6: ")) 

#add grades enetered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#To DO: determine lowest, highest, sum and average of the grades

low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

# determine letter grade for average

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"


#results

print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average: {average:.2f}")
print(("-----------------------------------"))

print(f"The letter grade is: {letter_grade}")
