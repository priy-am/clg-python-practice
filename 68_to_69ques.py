# 68. Write a program to create a Stack for storing only odd numbers out of all the numbers entered by the user. Display the content of the Stack along with the largest odd number in the Stack. (Hint. Keep popping out the elements from stack and maintain the largest element retrieved so far in a variable. Repeat till Stack is empty)

def is_odd(num):
    return num % 2 != 0

stack = []

print("Enter a done to stop entering numbers.")
while True:
    try:
        num = input("Enter a number: ")
        if num.lower() == 'done':
            break
        num = int(num)
        if is_odd(num):
            stack.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if not stack:
        print("No odd numbers were entered.")

if stack:
    stack.sort(reverse=True)  # Sort stack in descending order
    largest_odd = stack[0]
    print("Stack content:", stack)
    print("Largest odd number in the stack:", largest_odd)
else:
    print("No odd numbers were entered.")


# 69 Write the program to convert infix expression into postfix expression and evaluate it .
'''
infix  a+b
postfix a b +
'''

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def is_operator(c):
    return c in precedence

def infix_to_postfix(expr):
    stack = []
    postfix = []
    for char in expr:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while (stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isnumeric():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)
    return stack[0]



a = infix_to_postfix("2+3*(4-5)")
print("Postfix expression:", a)
print("Evaluated result:", evaluate_postfix(a))

