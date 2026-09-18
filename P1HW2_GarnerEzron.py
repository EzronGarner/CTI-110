# Ezron Garner
# 09/18/2026
# P1HW2 
# User enters budget and the budget they have left is outputted

print ("----This program calculates and displays travel expenses----")

budget = int(input("Enter budget:  "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas?  "))
hotel = int(input("How much do you think you will spend on hotel?  "))
food = int(input("Last, how much do you need for food?  "))

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)

print("Fuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)

print("Remaining balance:", budget - (gas + hotel + food))