import sys
def add(num1, num2):  
    add = num1 + num2       
    return add             

def sub(num1, num2):
    sub = num2 - num1
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

num1 = float(sys.argv[1])  # Taking inputs as arguments from command line and converting them to integers
operation = sys.argv[2] # Taking the operation as argument from command line
num2 = float(sys.argv[3]) # Taking inputs as arguments from command line and converting them to integers.

if operation == 'add':
    print('Addition:', add(num1, num2)) 
elif operation == 'sub':
    print('Substraction:', sub(num1, num2))
elif operation == 'mul':
    print('Multiplication:', mul(num1, num2))