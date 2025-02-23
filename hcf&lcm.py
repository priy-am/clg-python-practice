# WAP find LCM and HCF 
num = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a = num
b = num2
while num2 != 0:
    num = num2
    num2 = num % num2
hcf = num
lcm = (a*b)//hcf
print(f"HCF is {hcf} and LCM is {lcm}")

# WAP to find roots of quadratic equation 
print("Enter coefficients of quadratic equation ax^2 + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + d**0.5)/(2*a)
    root2 = (-b - d**0.5)/(2*a)
    print(f"Roots are {root1} and {root2}")
elif d == 0:
    root = -b/(2*a)
    print(f"Root is {root}")
else:
    real = -b/(2*a)
    img = (-d)**0.5/(2*a)
    print(f"Roots are {real} + {img}i and {real} - {img}i")