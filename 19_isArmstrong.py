#19  WAP to check whether a number is armstrong or not 
num = int(input("Enter a number: "))
# what is armstrong number? 153 -> 1^3 + 5^3 + 3^3 = 153
# 153 -> 3 digits
# 1234 -> 4 digits
sum = 0
a = num
while a > 0:
    sum += (a%10)**3
    a = a//10

if sum == num:
    print("Armstrong")
else:
    print("Not armstrong")