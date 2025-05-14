# 62. WAP to get input an integer and raise value error exception , if the input is not a valid integer. 
try:
    a = int(input("Enter a value of integer:- "))
    print(a)
except ValueError as e:
    print("Invalid! Please enter a valid integer.", e)


# 63. WAP to that the user to get 2 inputs and raise a type error exception if the input are not having numerical value .

try:
    a = float(input("Enter a value of a:- "))
    b = float(input("Enter a value of b:- "))
    print(f"Sum of {a} and {b} is {a + b}")
except ValueError :
    raise TypeError("Both inputs must be numerical values (int or float).")