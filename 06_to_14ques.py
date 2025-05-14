# 6. WAP to find sum of digits of 3 digit number 
num = int(input("Enter a 3 digit number: "))
sum = 0 
while num > 0:
    sum += num%10   # 234 -> 4, 23 -> 3, 2 -> 2
    num = num//10
print(f"Sum of digits is {sum}")

# 7. WAP to add 1 to all digits of 3 digit number 
num = int(input("Enter a 3 digit number: "))
new_num = 0   # 345-> 456
i =0
while num > 0:
    new_num = new_num + (num%10 + 1)*10**i
    num = num//10
    i += 1
print(f"New number is {new_num}")


# 8. WAP to calculate number of currency notes of 100, 50 and 10 
amount = int(input("Enter amount: "))
hundred = amount//100
amount = amount%100
fifty = amount//50
amount = amount%50
ten = amount//10
print(f"100 notes: {hundred}, 50 notes: {fifty}, 10 notes: {ten}")
# 9. WAP to check whether the number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# 10. WAP to check whether the year entered by user is leap year or not 
year = int(input("Enter a year: "))
if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
# 11. WAP to find greatest of 3 number 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print(f"{a} is greatest")
elif b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
# 12. WAP to find average and percentage of a student having 5 subjects 
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int (input("Enter marks of subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total/5
percentage = (total/500)*100
print(f"Average is {average} and percentage is {percentage}")
# 13. WAP to check whether number entered is character or alphabet or special character 
char = input("Enter a character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Number")
else:
    print("Special character")
# 14. WAP to check if character is vowel or consonant 
char = input("Enter a character: ")
if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
