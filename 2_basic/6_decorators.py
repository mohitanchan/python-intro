

""" 1. In Python, functions are first-class objects. ------------------------------------------
 This means that functions can be passed around and used as arguments """
def say_hello(name):
    print(f"Hello {name}")

def greeter(greeter_func):
    greeter_func("Bob")

greeter(say_hello)

""" 2. Inner function------------------------------------------ """
def parent():
    print("Inside parent")

    def first_child():
        print("First Child")

    def second_child():
        print("Second Child")

    first_child()
    second_child()

parent()

""" 3. Returning Functions From Functions------------------------------------------ """
def parent(num):
    def first_child():
        print("First Child")

    def second_child():
        print("Second Child")

    if num == 1:
        return first_child()
    else:
        return second_child()

parent(1)
parent(2)

""" Decorators------------------------------------------------------------"""
def mydecorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# Block_1
def say_hello():
    print("Hello")

say_hello = mydecorator(say_hello)
say_hello()

# Block_2
@mydecorator
def say_bye():
    print("Bye")
say_bye()
Block_1 and Block_2 are same
