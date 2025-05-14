# 1. Implement a queue using Python’s built-in list methods.( Hint: Use append() to enqueue elements.Use pop(0) to dequeue elements.Check if the list is empty before dequeuing) 

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"
    
    def display(self):
        return self.items
    
q = Queue()

# Enqueue some elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueuing:", q.display())

# Dequeue elements
print("Dequeued:", q.dequeue())
print("Queue after dequeuing:", q.display())

# Try dequeueing from empty queue
q.dequeue()
q.dequeue()
print("Dequeued from empty queue:", q.dequeue())