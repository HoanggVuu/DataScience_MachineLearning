'''
Python functions are reusable blocks of code that perform specific tasks.
They help organize your code, make it more modular, and enable code reusability.
Functions are defined using the def keyword and can accept inputs (parameters) and return outputs.

Parameters: these are the variables defined in a function's signature that accept input values.
Arguments: these are the actual values passed to a function's parameters when it is called
'''

##########################################

'''
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional

+ def keyword: Starts the function definition
+ Function name: Should follow Python naming conventions (snake_case)
+ Parameters: Input values in parentheses (optional)
+ Colon (:): Marks the start of the function body
+ Indented code block: The function's implementation
+ return statement: Returns a value to the caller (optional)
'''

##########################################

'''
Flow of contents:
1. Define a function using def: without parameters, with parameters, with default parameters.
2. Return a value using "return" statement.
3. Constraint the data type of parameters using type hints.
4. Positional arguments: passing arguments in the order of parameters.
5. Keyword arguments: passing arguments by explicitly specifying the parameter names.
6. Default arguments: parameters with default values that can be omitted when calling the function.
7. *args (Variable Positional Arguments): allows passing a variable number of positional arguments to a function.
8. **kwargs (Variable Keyword Arguments): allows passing a variable number of keyword arguments to a function.
'''


#------------------------------------------------------------------------------------------------------------#
#----------------------------------- 1. Define a function using def -----------------------------------------#
#------------------------------------------------------------------------------------------------------------#

#######################################
## Basic function without parameters ##
#######################################

def greet():
    """Simple greeting function."""
    print("Hello, World! This is a basic function without parameters.")


# Call the function
greet()
# Hello, World! This is a basic function without parameters.


##############################
## Function with parameters ##
##############################

def add_numbers(x, y):
    """Add two numbers."""
    print(f"{x} + {y} = {x + y}")


# Call the function with arguments
add_numbers(
    x = 5, # x and y are parameters
    y = 10 # 5 and 10 are arguments passed to the function's parameters
)
# 5 + 10 = 15


# Call the function with positional arguments
add_numbers(3, 7)
# 3 + 7 = 10


######################################
## Function with default parameters ##
######################################

def customer_info(name, age=30, job="Unknown"):
    """Display customer information with a default age and job"""
    print(f"Customer Name: {name}, Age: {age}", f"Job: {job}")

# Call the function with default parameters
customer_info("Alice")
# Customer Name: Alice, Age: 30 Job: Unknown


# Call the function with custom parameters (repalacing default values)
customer_info("Bob", 25, "Engineer")
# Customer Name: Bob, Age: 25 Job: Engineer


#------------------------------------------------------------------------------------------------------------#
#------------------------------- 2. Return a value using "return" statement ---------------------------------#
#------------------------------------------------------------------------------------------------------------#

# "return" statement is used to exit a function and return a value to the caller.

###############
## Example 1 ##
###############
def square(number):
    """Return the square of a number."""
    return number * number

# Call the function and store the returned value
result = square(4)
print(f"The square of 4 is: {result}")


###############
## Example 2 ##
###############

def input_customer_info():
    """Input customer information and return it as a dictionary."""
    name = input("Enter customer name: ")
    age = int(input("Enter customer age: "))
    job = input("Enter customer job: ")
    
    return {"name": name, "age": age, "job": job}

# Call the function and store the returned dictionary
customer_data = input_customer_info()

print(f"Customer Data: {customer_data}")
#Customer Data: {'name': 'Zetharax', 'age': 150000, 'job': 'Creator of the world'}

#------------------------------------------------------------------------------------------------------------#
#--------------------------- 3. Constraint the data type of parameters using type hints ---------------------#
#------------------------------------------------------------------------------------------------------------#

def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result (also integer)."""
    return a * b