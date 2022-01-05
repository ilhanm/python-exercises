from turtle import Turtle
from turtle import Screen
from random import random
from random import choice
tosbik=Turtle()
screen= Screen()

tosbik.pensize(1)
tosbik.speed("fastest")
directions=[0,90,180,270]
for i in range(72):
    tosbik.color(random(),random(),random())
    tosbik.circle(100)
    #tosbik.setheading(tosbik.heading()+5)
    tosbik.left(5)

screen.exitonclick()