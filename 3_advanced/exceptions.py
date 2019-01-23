

"""Try and Catch"""
def divide(a, b):
    c = 0
    try:
        c = a/b
    except ZeroDivisionError as err:
        print("Error >> ", err)
    finally:
        print("Good bye")
    return c

divide(10, 0)


"""Throw (raise) an Exception"""

def check_positive_num(num):
    if num < 0:
        raise Exception("Number less than zero")
    return True;

def my_func(num):
    check_positive_num(num)
    print("success")

my_func(1)
my_func(-1)
