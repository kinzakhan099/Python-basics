import math

def calculate(radius):
    circumference=2*math.pi*radius
    square_root=math.sqrt(radius)
    print("Output before importing specific functions:")
    print(f"Circumference: {circumference}")
    print(f"Square root: {square_root}")
calculate(5)

from math import pi, sqrt  

def calculate(radius):
    circumference=2*pi*radius
    square_root=sqrt(radius)
    print("\nOutput after importing specific functions:")
    print(f"Circumference: {circumference}")
    print(f"Square root: {square_root}")
calculate(5)