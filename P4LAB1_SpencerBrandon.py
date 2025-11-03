# Brandon Spencer
# 11-1-25
# P4LAB1
# Drawing Shapes with Turtle Python

import turtle
import time


screen = turtle.Screen()
screen.bgcolor("lightblue")  

t = turtle.Turtle()
t.color("green")
t.pensize(2)
t.speed(5)

t.penup()
t.goto(-50, -50)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50, 50)
t.pendown()


i = 0
while i < 3:
    t.forward(100)
    t.left(120)
    i += 1

turtle.done()

