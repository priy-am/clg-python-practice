# 17 WAP to find number is prime or not 
num = int(input("Enter a number: "))
flag = 0
for i in range(2, num//2+1):
    if num % i == 0:
        flag = 1
        break
if flag == 0:
    print("Prime")
else:
    print("Not prime")

#18  WAP to display grade obtained from 5 subjects marke in final exam of a student 
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total/5
if avg >= 90:
    print("Grade A")
elif avg >= 80:
    print("Grade B")
elif avg >= 70:
    print("Grade C")
elif avg >= 60:
    print("Grade D")
else:
    print("Grade F")