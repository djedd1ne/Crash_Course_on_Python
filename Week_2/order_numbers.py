#!/usr/bin/env python3
# This function compares 2 numbers and return them
# in increasing order
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1
	
# Function call
smaller , bigger = order_numbers(100, 99)
# Print in order
print(smaller, bigger)