#!/usr/bin/env python3
# This function converts fluid ounces to milliliters 
def convert_volume(fluid_ounce):
	ml = fluid_ounce * 29.5
	return ml
# Call the conversion from whithin the print() function
print ("The volume in milliliters is " + str(convert_volume(2)))

# Call the function again and double the ounces
print("The volume in milliliters is " + str(convert_volume(2) * 2))

# Alternate calculation
# print("The volume in milliliters is " + str(convert_volume(4)))