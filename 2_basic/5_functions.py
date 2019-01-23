

def sayhello():
    print("Hello")

def add(num1, num2):
    print(num1 + num2)
    return num1 + num2

sayhello()
add(1, 3)


""" default values to params """
def greet(name="User", time="Day"):
    print(f"Good {time} {name}")

greet()
greet("Miles")
greet("Miles", "Morning")
greet(time="Evening",name="Miles")

"""Arbitrary number of parameters"""
def print_params(*args):
    for arg in args:
        print(arg)

print_params(1, 3, 5, 6, 7, 9, 4, "India", False)

def print_dict_params(*args, **kwargs):
    for arg, val in kwargs.items():
        print(f"{arg} : {val}")

print_dict_params(country="India", capital="New Delhi", states=29, is_independent=True)
