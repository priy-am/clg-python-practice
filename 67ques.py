# 67. write a program to create a STACK (stack of glasses as given in Figure 3.2) in which we will:
# * insert/delete elements (glasses) 
# * check if the STACK is empty (no glasses in the stack) 
# * find the number of elements (glasses) in the STACK 
# * read the value of the topmost element (number on the topmost glass) in the STACK 

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        print(f"Inserted {item} into the stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return 
        item = self.stack.pop()
        print(f"Removed {item} from the stack.")
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        if self.is_empty():
            print("stack is empty. No top element.")
            return
        return self.stack[-1]
    
# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Is the stack empty?", stack.is_empty())
    
    print("Number of elements in the stack:", stack.size())
    print("Top element in the stack:", stack.top())
    
    stack.pop()
    
    # Check if the stack is empty again
    print("Is the stack empty?", stack.is_empty())