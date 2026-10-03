# Ezron Garner
 # 10/3/26
 # P2LAB2
 # write a program that creates a dictionary where the key and value pairs are as follows.

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#get keys from dictionary

cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")
#user input a car
car_name = input("Enter a vehicle to see it's MPG: ")

#Get MPG for the given car
car_mpg = cars.get(car_name)
print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Number of miles the user wants to drive
miles = float(input(f"Enter the number of miles you want to drive the {car_name}? "))

#calculate the number of gallons needed to drive the given miles
gallons_needed = miles / car_mpg

#Display the results

print(f"You will need {gallons_needed:.2f} gallon(s) of gas to drive {miles} miles in the {car_name}.")
