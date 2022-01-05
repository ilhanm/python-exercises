from turtle import Turtle
from turtle import Screen
from random import random
from random import choice
tosbik=Turtle()
screen= Screen()

tosbik.pensize(2)
tosbik.speed("fastest")
directions=[0,90,180,270]
for i in range(40):
    #tosbik.color(random(),random(),random())
    tosbik.forward(i)
    tosbik.right(directions[i%2*2])
    tosbik.forward(i)
    for j in directions:
        tosbik.circle(10+j*2)
    tosbik.circle(50)

screen.exitonclick()