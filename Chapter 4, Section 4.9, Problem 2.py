#-------------------------------------------------------------------------------
# Name:        Chapter 4, Section 4.9, Problem 2
# Purpose:
#
# Author:      Lilyj
#
# Created:     16/09/2025
# Copyright:   (c) Lilyj 2025
# Licence:     <your licence>
#---------------------------------------------------------------------------
import turtle
scrn = turtle.Screen()
scrn.screensize(500, 500)
scrn.bgcolor('lime green')
lily = turtle.Turtle()
lily.shape('turtle')
lily.color('white')
length = [20, 40, 60, 80, 100]

def square(y):
    x=-y/2
    lily.penup()
    lily.goto(x, y/2)
    lily.pendown()
    for side in range(4):
        lily.forward(y)
        lily.right(90)

for num in length:
    square(num)

turtle.Screen().exitonclick()
