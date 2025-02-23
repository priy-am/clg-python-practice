# 1. WAP to find sum of 2 numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum of {a} and {b} is {a+b}")

# 2. WAP for swapping of 2 numbers 
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
temp = a
a = b
b = temp
# 3. WAP to reverse a 3 digit number 
num = int(input("Enter a 3 digit number: "))
rev = 0
# 123 -> 321 
while num > 0:
    rev = rev*10 + num%10
    num = num//10
print(f"Reverse of the number is {rev}")
# 4. WAP to find area and perimeter of rectangle 
length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
area = length * breadth
perimeter = 2*(length + breadth)
print(f"Area of rectangle is {area} and perimeter is {perimeter}")
# 5. WAP to find area and circumference of a circle 
radius = int(input("Enter radius of circle: "))
print(f"Area of circle is {3.14*radius*radius} and circumference is {2*3.14*radius}")
