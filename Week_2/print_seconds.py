#!/usr/bin/env python3
# A function that takes 2 parameters: hours, minutes and seconds
# and converts them to seconds
def print_seconds(hours, minutes, seconds):
	print(hours * 3600 + minutes * 60 + seconds)

# Call the function
print_seconds(1, 2, 3)