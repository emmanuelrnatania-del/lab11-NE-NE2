#https://github.com/emmanuelrnatania-del/lab11-NE-NE2.git
#Partner 1: Natania Emmanuel
#Partner 2: Natania Emmanuel

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be >0 and !=1")
    if b <= 0:
        raise ValueError("Logarithm argument must be >0")
    return math.log(b, a)

def exp(a, b):
    return a ** b