from PIL.Image import new
import colorgram

from turtle import Turtle
from turtle import Screen
import turtle
import random
#turtle.colormode(255)
abidin=Turtle()
abidin.speed("fastest")
# rgb_colors=[]
# toptencolors=colorgram.extract("dots.jpg",10)
# print(toptencolors)

# for color in toptencolors[1:]:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
rgb_colors=[(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57)]

def cizgiler():
    abidin.pensize(2)
    abidin.penup()
    abidin.setposition(-120,-90)
    for i in range(10):
        for j in range(10):
            abidin.color(random.choice(rgb_colors))
            abidin.forward(30)
            if j%2==0: abidin.pendown()
            else: abidin.penup()
        abidin.setpos(-120,abidin.ycor()+30)

abidin.penup()
abidin.setposition(-150,-150)
for i in range(10):
    for j in range(10):
        #abidin.color(random.choice(rgb_colors))
        abidin.color((random.random(),random.random(),random.random()))
        abidin.begin_fill()
        abidin.circle(10)
        abidin.end_fill()
        abidin.penup()
        abidin.forward(50)
        abidin.pendown()
    abidin.penup()
    abidin.setpos(-150,abidin.ycor()+50)




screen=Screen()
screen.exitonclick()

