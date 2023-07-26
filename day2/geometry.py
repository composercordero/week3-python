import math

def get_area(radius):
    return f"The area of a circle with radius {radius} is {math.pi*(radius**2)}"

def get_hypotenuse(a,b):
    return f"the hypotenuse of a right angle with sides of {a} in and {b} in is {math.sqrt(a ** 2 + b ** 2)} in"


# from math import pi, sqrt

# def get_area(radius):
#     return f"The area of a circle with radius {radius} is {pi*(radius**2)}"

# def get_hypotenuse(a,b):
#     return f"the hypotenuse of a right angle with sides of {a}in and {b}in is {sqrt(a ** 2 + b ** 2)} in"
# # No need to add math in from of the functions because we imported those functions from math.
