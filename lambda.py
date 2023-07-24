# Create a lambda function to add 25 to a given number
add_25 = lambda x: x + 25

# Take input from the user as an integer
try:
    number = int(input("Enter a number: "))
    
    # Using the lambda function to add 25 to the input number
    result = add_25(number)
    
    # Output
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer number.")
