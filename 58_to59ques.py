# 58. Write a program to handle zero division exception when dividing a number by zero .  
try:
    a = int(input("Enter a value to divide:- "))
    b = int(input("Enter b value to divide by:- "))
    c = a / b
    print(f"Result of {a} / {b} = {c}")
except ZeroDivisionError as e :
    print("Invalid!", e)


# 59. Write a program to handle array out of bound exception .

try:
    arr = [1, 2, 3, 4, 5]
    index = int(input("Enter the index to access:- "))
    print(f"Element at index {index} is {arr[index]}")
except IndexError as e:
    print("Invalid! the element contain 4 index. ! ", e)