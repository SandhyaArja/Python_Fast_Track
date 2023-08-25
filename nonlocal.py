def outer_function():
    outer_var = 10  # Outer variable

    def inner_function():
        nonlocal outer_var  # Declare the use of the outer variable
        outer_var = 20     # Modify the outer variable inside the inner function

    inner_function()  # Call the inner function
    print("Outer variable after inner function:", outer_var)

outer_function()
