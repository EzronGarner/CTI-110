#Ezron Garner
#10/3/26
#P2LAB1
#The program will calculate the diameter, circumference, and area of a circle.

#import math module to use the constant, math.pi
import math

#Get radius from user
radius = float(input("Enter the radius of the circle: "))
print()

#calculate diameter
diameter = 2 * radius

#display diameter with 1 decimal place
print(f"The diameter of the circle is: {diameter:.1f}")

#calculate circumference
circumference = 2 * math.pi * radius

#display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate area
area = math.pi * radius**2

#display area with 3 decimal places
print(f"The area of the circle is: {area:.3f}")