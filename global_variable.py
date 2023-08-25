global_variable = 10  # Global variable

def modify_global():
    global global_variable  # Declare the use of the global variable
    global_variable = 20    # Modify the global variable

print("Before modification:", global_variable)  # Output: Before modification: 10

modify_global()  # Call the function to modify the global variable

print("After modification:", global_variable)  # Output: After modification: 20



