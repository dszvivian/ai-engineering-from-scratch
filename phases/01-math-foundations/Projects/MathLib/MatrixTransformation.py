# We are Experimenting only with 2*2 Matrix. Cuz it's easier for calculation and easier to visualize.

import math
from Matrices import Matrix

def rotation(theta):
    return Matrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])

def scaling(sx, sy):
    return Matrix([[sx, 0],[0,sy]])

def shearing(zx, zy):
    return Matrix([[1, zx],[zy,1]])

def reflection_x():
    return Matrix([[1, -1],[0,1]])

def reflection_y():
    return Matrix([[1, 0],[-1,1]])

def broadcasting(): # ie: This happens while Matrix @ Vec multiplication.
    pass


if __name__  == "__main__":
    
    mata = Matrix([[1,3], [2,4]])
    
    theta = math.pi / 4 # ie: at pi /4 both sin and cos are same
    
    print(f"Matrix A: {mata}")
    print(f"Rotation: {mata @ rotation(theta=theta)}")
    print(f"Scaling: {mata @ scaling(2, 1)}")
    print(f"shearing: {mata @ shearing(2, 1)}")
    print(f"Reflection X: {mata @ reflection_x()}")
    print(f"Reflection Y: {mata @ reflection_y()}")