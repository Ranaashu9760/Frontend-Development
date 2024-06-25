# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the columns.
    for column in range(n1, n2):

        # The nested for loop will create the rows.
        for row in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
              print(column*row, end=" ")

        # The row ends when the upper range value is encountered within the 
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
matrix(1, 4)
# Should print:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 

print()
for outer_loop in range(10):
    for inner_loop in range(outer_loop):
        print(inner_loop)
        

print()
for n in range(11, 0, -2):
    if n % 2 != 0:
        print(n, end=" ")  

print()
starting_number = 18
while starting_number >= 0:
    print(starting_number, end=" ")
    starting_number -= 3   

print()
# This function accepts a CEO's salary as a variable. 
# It counts the number of digits in the salary and 
# returns the sentence like:
# "The CEO has a 6-figure salary."
def X_figure(salary):
    
    # Initializes the counter as an integer.
    tally = 0

    # The if-statement checks if the variable "salary" 
    # is equal to 0.
    if salary == 0:
        # If true, then it increments the counter to 
        # show there is 1 digit in 0.
        tally += 1

    # The while loop starts to run while the "salary"
    # is greater than or equal to 1 (the loop will 
    # not run if the "salary" is 0).
    while salary >= 1:

        # The body of the while loop counts the digits 
        # in "salary" by counting the number of times 
        # "salary" can be divided by 10 until "salary" 
        # is no longer >= 1.
        salary = salary/10

        # Add 1 to the counter to tally the number of 
        # times the loop runs.
        tally += 1

    # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally
 
# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# Should print"The CEO has a 7-figure salary."

print()
# This function will accept two integer variables: the floor
# number that a passenger "enter"s an elevator and the floor
# number the passenger is going to "exit". Then, the function
# counts up or down from the two floor numbers.
def elevator_floor(enter, exit):
    # The "floor" variable will be used as a counter and to  
    # print the floor numbers. The "elevator_direction"
    # variable will hold the string "Going up: " or 
    # "Going down: " plus the count up or down of the 
    # "floor" numbers.
    floor = enter
    elevator_direction = ""

    # If the passenger enters the elevator on a floor that  
    # is higher than the destination floor:
    if enter > exit:
        
        # Then the "elevator_direction" string will be 
        # initialized with the string "Going down: ".
        elevator_direction = "Going down: "

        # While the "floor" number is greater than or  
        # equal to the exit floor number:
        while floor >= exit:
            # The "floor" number is converted to a string 
            # and is appended to the string variable 
            # "elevator_direction".
            elevator_direction += str(floor)

            # If the "floor" number is still greater than  
            # the exit floor number:
            if floor > exit:

                # A pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor > exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer greater than the "exit" 
                # variable. 
                elevator_direction += " | "
                
                # Decrement the "floor" number as the elevator 
                # goes down.
            floor -= 1

    # Else, it is implied that the passenger is entering the  
    # elevator on a floor that is lower than the destination 
    # floor.
    else:

        # The "elevator_direction" string will be initialized 
        # with the string "Going up: ".
        elevator_direction = "Going up: "
        
        # While the "floor" number is less than or equal to the 
        # "exit" floor number:
        while floor <= exit:

            # Convert the the "floor" number to a string and append 
            # it to the string variable "elevator_direction".
            elevator_direction += str(floor)

            # If the entry floor number is still less than the exit 
            # floor number:
            if floor < exit:

                # The pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor < exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer less than the "exit" 
                # variable. 
                elevator_direction += " | "

            # Increments the "floor" number as the elevator goes up.
            floor += 1

    # Returns the string holding the elevator direction (Going down or 
    # Going up) along with the floor countdown or count up.
    return elevator_direction


# Call the function with 2 integer parameters. 
print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2

