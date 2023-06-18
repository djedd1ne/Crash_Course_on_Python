#!/usr/bin/env python3
# The function calculates the number of days in a variable
# number of years, months and days
def find_total_days(years, months, days):
	my_days = (years * 365) + (months * 30) + days
# Use "return" keyword to send the result of the "my_days"
# to the function call
	return my_days

# Function call
print (find_total_days(2,5,23))