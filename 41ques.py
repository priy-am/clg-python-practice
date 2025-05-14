import re
# 41. WAP to segregate all the words, nos. , special characters in a paragraph into 3 different list.
def segregate_text(para):
    words = re.findall(r'[A-Za-z]+', para)
    number = re.findall(r'\d', para)
    special_char = re.findall(r'[^A-Za-z0-9\s]', para)
    return words, number, special_char


paragraph = "Hello, my age is 20! I have $100 and 2 dogs."

words, number, special_char = segregate_text(paragraph)

print("Words:", words)            
print("Numbers:", number)       
print("Special Characters:", special_char)