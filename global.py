global_variable = 10  # Global variable

def modify_global():
    global global_variable  # Declare that we want to modify the global variable
    global_variable = 20    # Modify the global variable inside the function

modify_global()  # Call the function to modify the global variable
print("Global variable:", global_variable)  # Output: Global variable: 20
