#!/usr/bin/env python3

import math

def main():
    x = 0
    piCircle = math.pi

    while x != 1:
        entrada=input("Choose a shape (triangle, rectangle, circle): ")
        if entrada == "triangle" or entrada == "rectangle" or entrada == "circle":
            if entrada == "triangle":
                baseTri = int(input("Give base of the triangle: "))
                heigTri = int(input("Give height of the triangle: "))
                print(F"The area is {baseTri*heigTri/2:.6f}")
            if entrada == "rectangle":
                widthRect = int(input("Give width of the rectangle: "))
                heightRect = int(input("Give height of the rectangle: "))
                print(F"The area is {widthRect*heightRect:.6f}")
            if entrada == "circle":
                radiCircle = int(input("Give radius of the circle: "))
                print(F"The area is {piCircle*radiCircle**2:.6f}")
        else:
            if entrada == "":
                break
            else:
                print("Unknown shape!")
if __name__ == "__main__":
    main()
