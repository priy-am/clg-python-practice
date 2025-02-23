# 20. WAP to perform various arithmetic expression on two numbers using match case statement Add, subtract,multiply, divide, integer division 
print("choose operation: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Integer division")
choice = int(input("Enter choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
match choice:
    case 1:
        print(f"Sum is {a+b}")
    case 2:
        print(f"Difference is {a-b}")
    case 3:
        print(f"Product is {a*b}")
    case 4:
        print(f"Division is {a/b}")
    case 5:
        print(f"Integer division is {a//b}")
    case _:
        print("Invalid choice")
# 21. WAP to display name of month by integer value given by user 
months =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input("Enter the integer value for month ")
print(f"{month} is integer value of {months[month]}")
