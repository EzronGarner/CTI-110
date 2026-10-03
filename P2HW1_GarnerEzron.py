# Ezron Garner
# 10/3/2026
# P2HW1
# User enters budget and the budget they have left is outputted

print ("----This program calculates and displays travel expenses----")

budget = int(input("Enter budget:  "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas?  "))
hotel = int(input("How much do you think you will spend on hotel?  "))
food = int(input("Last, how much do you need for food?  "))

print("------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} {budget}")

print(f"{'Fuel:':<20} {gas}")
print(f"{'Accommodation:':<20} {hotel}")
print(f"{'Food:':<20} {food}")

print(f"{'Remaining balance:':<20} {budget - (gas + hotel + food)}")
