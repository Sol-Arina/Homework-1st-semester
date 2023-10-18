from math import pi

def rectangle(a, b):
    s = a * b
    return s

def square(a):
    s = a * a
    return s

def triangle(a, h):
    s = a * h * 0,5
    return s

def sphere(r):
    s = ((r ** 2) * pi) * 4 / 3
    return s

