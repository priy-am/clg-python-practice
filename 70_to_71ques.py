# 70 Write a program to reverse a string using a stack. 

def reverse_string(string):
    stack = []
    for i in string:
        stack.append(i)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Example usage
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)


# 71. Write the program to check balanced parenthesis using stack

def is_balanced_parentheses(expr):
    stack = []
    brackets = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    return len(stack) == 0


expr = input("Enter an expression: ")
if is_balanced_parentheses(expr):
    print("✅ Parentheses are balanced.")
else:
    print("❌ Parentheses are NOT balanced.")