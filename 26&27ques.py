# 26. WAP to calculate sum of series 1+3/3!+5/5!+....2n-1/2n-1! By defining function 
def fact(n):
    if(n==1 or n == 0):
        return 1
    return n*fact(n-1)

sum = 0

num = int(input("enter the value of n:- "))
for i in range(1, num+1):
    facti = fact(2*i-1)
    sum = sum + (2*i-1)/facti

print(f"The answer is {sum}")




# 27. WAP to find sum of series 1+2/2!+5/5!+.....

# sum2 = 1
# n = int(input("enter The value of n :- "))
# for i in range(2, n+1):
#     factAns = fact(2*1)
#     sum2 += 