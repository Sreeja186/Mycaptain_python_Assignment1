# import math module
from math import pi
 
# take input from user
r = float(input ("Input the radius of the circle : "))
 
# compute the area from radius of a circle given by user
calculateArea = str(pi * r**2);
 
#print result
print ("The area of the circle with radius " + str(r) + " is: " + calculateArea)
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
