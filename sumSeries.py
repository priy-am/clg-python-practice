# 22. WAP to find sum of series 1+x+x^2+...+x^n-1
x = int(input("Enter the value of x:- "))
n = int(input("Enter the value of n:- "))
sum = 1
for i in range(1, n+1):
    sum = sum + x**i
print(f"The sum of series {sum}")
# 23. WAP to find sum of series y=x+x^3+x^5+...+x^2n-1 and y=x+x^2+x^4+...+x^2n
x1 = int(input("Enter the value of x"))
n1 = int(input("Enter the value of y:- "))
sum1 = 0
for i in range( 1, n1+1):
    sum1 = sum1 + x1**(2*n1-1)
print(f"The Sum of odd series is {sum1}")

sum2 = 0
for i in range(1, n1+1):
    sum2 =sum2 + x1**(2*n)
print(f"the even sum series is {sum2}")