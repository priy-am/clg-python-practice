import math
# 60.  Program to find distance of point using __init__() 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self):
        return math.sqrt(self.x**2 + self.y**2)
p1 = Point(3, 4)
print(f"Distance of point {p1.x}, {p1.y} from origin is {p1.distance_to_point()} units")

# 61. Program to implement student record management system using concept of instance and static methods in class.

class Student:
    def __init__(self, name, rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollNo}, Marks: {self.marks}")
    
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Updated Marks for {self.name} is {self.marks}")

    @staticmethod
    def show_help():
        print("\nThis is a Student Record Management System")
        print("You can add, view, or update student records\n")
    
# Example usage
s1 = Student("John Doe", 101, 85)
s1.display()
s1.update_marks(90)
s1.show_help()