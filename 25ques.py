# 25. WAP to find factorial of a number by defining a function 
def fact(n):
    if(n==1 or n == 0):
        return 1
    return n*fact(n-1)

num = int(input("Enter the number:- "))
print(f"the factorial is :- {fact(num)}")