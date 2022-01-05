#191den devam ederim
from turtle import Screen
import time
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

mysnake=Snake()

screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")


game_is_on=True
while(game_is_on):    
    screen.update()
    time.sleep(0.1)
    mysnake.move()
    

screen.exitonclick()