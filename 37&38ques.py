# 37. WAP to find no. of occurrences of a particular character in a string.
s = 'Anantaa'
occurrence = 0
for i in s:
    if(i.lower() == 'a' ):
        occurrence += 1
print(occurrence)
# 38. WAP to remove all occurrences of a particular sub-string in a string.

name = 'Anantaa'

newName = name.replace('n', '')
print(newName)