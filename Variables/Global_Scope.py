x = 5 # Global variable
def my_function():
    global x # Modify the global variable
    x = 23
    print(x)
my_function()