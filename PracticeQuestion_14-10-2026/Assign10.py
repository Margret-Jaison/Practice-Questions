# Question 13: Student class
# Create a class Student with:
# ●	A constructor that accepts name, roll number, and marks.
# ●	A method display_details() that prints all details.
# ●	A method check_result() that returns "Pass" if marks are at least 40, otherwise "Fail".
# Create three objects and display their results
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")

    def check_result(self):
        return "Pass" if self.marks >= 40 else "Fail"
Student1=Student("Alice", 1, 85)
Student1.display_details()
print(Student1.check_result())
Student2=Student("Bob", 2, 35)
Student2.display_details()
print(Student2.check_result())
Student3=Student("Charlie", 3, 55)
Student3.display_details()
print(Student3.check_result())