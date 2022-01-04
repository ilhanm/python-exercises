from turtle import Turtle
from turtle import Screen
from random import random
from random import choice
tosbik=Turtle()
screen= Screen()


directions=[0,90,180,270]
for _ in range(50):
    tosbik.color(random(),random(),random())
    tosbik.right(choice(directions))
    tosbik.forward(50)

screen.exitonclick()