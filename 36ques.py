# 36. Suppose we have a string s = '1.3, 3.45, 2.3'. WAP a program to perform sum of string
s = '1.3, 3.45, 2.3'

number = s.split(", ")
total = sum(map(float, number))
print(f"The total is {total}")