
"""Inheritance Syntax"""
class Parent:
    def __init__(self):
        self.name = "Parent"

class Child(Parent):
    def greet(self):
        print(f"Hello {self.name}")

child = Child()
print(child.greet())

"""Inheritance Example -------------------------------------------"""
from classes import MyDate

class MyDateTime(MyDate):

    def __init__(self, day, month, year, hour, min):
        MyDate.__init__(self, day, month, year)
        self.hour = hour
        self.minute = min

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year} {self.hour}:{self.minute}"


mydatetime = MyDateTime(23, 1, 2019, 12, 30)
print(mydatetime)
