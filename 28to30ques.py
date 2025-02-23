# WAP to print Fibonacci series using recursion 

def fibbonacci(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return fibbonacci(n-1)+ fibbonacci(n-2)

n = int(input("Enter the number :- "))
print(f"The answer is {fibbonacci(n)}")

# 29. WAP to display squares of n natural numbers 
num = int(input("Enter the the value of n :- "))

for i in range(1,n+1):
    print(f"The square of {i} is {i**2}")

# 30. WAP to display first n multiples of x
def multiples(x, n):
    for i in range(1, n+1):
        print(f"{x} X {i} = {x*i}")

n = int(input("Enter the number value of n:- "))
x = int(input("Enter the number value of x:- "))
multiples(x,n)
