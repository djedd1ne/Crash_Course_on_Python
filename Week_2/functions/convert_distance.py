#!/usr/bin/env python3
# Approximately 1.6 km in 1 mile
def convert_distance(miles):
	km = miles * 1.6
	return km

# Do not indent any of the following lines
my_trip_miles = 55

# Convert to km by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# Print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# Calculate the round-trip by doubeling the result
print ("The round-trip in kilometers is " + str(my_trip_km * 2))