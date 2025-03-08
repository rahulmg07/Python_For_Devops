num1 = 10
num2 = 20
def addition(): # Function
    add = num1 + num2
    print(add)

def substraction(): #2nd Function
    sub = num2 - num1
    print(sub)

def multiplication(): #3rd Function
    mul = num1 * num2
    print(mul)

# Calling the functions
addition()
substraction()
multiplication()

# Correct way of Writing the functions:

def addition(num1, num2):  # Taking inputs as arguments
    add = num1 + num2      # Performing the operation 
    return add             # Returning the output

def substraction(num1, num2):
    sub = num2 - num1
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

print('Addition:', addition(50, 10)) # calling the function with arguments
print('Substraction:', substraction(5, 10))
print('Multiplication:', multiplication(10,20))
