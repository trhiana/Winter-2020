"""
Rhiana Thelemaque
Python Projects
"""

from random import randint
from turtle import Turtle
from turtle import *


"""Creating the race tracks"""
speed(5)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align = 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


first_tutle = Turtle()
first_tutle.color('black')
first_tutle.shape('turtle')
first_tutle.penup()
first_tutle.goto(-160, 100)
first_tutle.pendown()

second_turtle = Turtle()
second_turtle.color('maroon')
second_turtle.shape('turtle')
second_turtle.penup()
second_turtle.goto(-160, 70)
second_turtle.pendown()

third_turtle = Turtle()
third_turtle.color('blue')
third_turtle.shape('turtle')
third_turtle.penup()
third_turtle.goto(-160, 40)
third_turtle.pendown()

fourth_turtle = Turtle()
fourth_turtle.color('grey')
fourth_turtle.shape('turtle')
fourth_turtle.penup()
fourth_turtle.goto(-160, 10)
fourth_turtle.pendown()

"""Turtles turn 360 degrees once they are at the starting line"""
for turn in range(10):
    first_tutle.right(36)
    second_turtle.right(36)
    third_turtle.right(36)
    fourth_turtle.right(36)

"""Turtle movements"""
for move in range(100):
    first_tutle.forward(randint(1, 5))
    second_turtle.forward(randint(1, 5))
    third_turtle.forward(randint(1, 5))
    fourth_turtle.forward(randint(1, 5))

input('Press <Enter> to close')