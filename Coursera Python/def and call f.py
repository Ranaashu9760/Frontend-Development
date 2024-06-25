def lucky_number(name):
     number = len(name ) * 10
     print("Hello " + name + " Your lucky number is " + str(number))

lucky_number("kay")
lucky_number("Cameron")

print()

def calculate(d):
    q = 3.14
    z = q*(d**2)
    print(z)
    
calculate(5)

print()

def circle_area(radius):
    pi = 3.14
    area = pi*radius**2
    print(area)
circle_area(2)

print()

# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in millimeters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in millimeters is " + str(convert_volume(2)*2))
# Alternative calculation:
print("The volume in millimeters is " + str(convert_volume(4)))

print()

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return (km)

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = 0.621371192 * (my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_miles))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(my_trip_miles*2))


print(10<1)



    