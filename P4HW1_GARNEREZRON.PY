#Ezron Garner
#10/30/26
#P4HW1
# This program asks the user to enter scores and determines the average and displays a letter grade based on the average.


#add grades enetered to a list
grades = []
user_num = int(input("How many scores do you want to enter? "))



for item in range(0, user_num):
    score=int(input(f"Enter score {item}: "))
    
    while score < 0 or score > 100:
        print ("INVALID Score entered!!!!")
        print ("Score should be between 0 and 100")
        score = int(input(f"Enter score {item }: ")) 

    grades.append(score)

#Lowest score etc
low = min(grades)
grades.remove(low)
average = sum(grades) / len(grades)



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
print("------Results------")
print(f"{'Lowest Score':<20}: {low:.1f}")
print(f"{'Modified List':<20}: {grades}")
print(f"{'Scores Average':<20}: {average:.2f}")
print(f"{'Letter Grade':<20}: {letter_grade}")
print("------------")