
# 64. Write a program that takes a list of numbers from the user and asks for an index. Handle cases where the index is out of range
'''
This are done in the previous code question number 59
'''

# 65. Write a program that tries to read a file. If the file does not exist, handle the error.

try:
    with open('priyam.txt', 'r')as f:
        content = f.read()
        print(content)
    print("File read successfully")
except FileNotFoundError as e:
    print("File not found. Please check the file name and path.")
    print(f"Error: {e}")


# 66. Write a program that takes an age input. If the user enters a negative number, raise a custom exception

class NegativeAgeError(Exception):
    def __init__(self):
        super().__init__("Age cannot be negative")

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAgeError
    print(f"Your age is {age}")
except NegativeAgeError as e:
    print("Error: ", e)