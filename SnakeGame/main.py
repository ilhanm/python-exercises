from turtle import Screen,Turtle, pos
import random, time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments=[]

for i in range(5):
    newSegment=Turtle()
    newSegment.penup()
    newSegment.color("white")
    newSegment.shape('square')
    newSegment.setx(i*20)
    segments.append(newSegment)
    
# [0][1][2]

game_is_on=True
while(game_is_on):
    screen.update()
    time.sleep(0.1)
    for seg_num in range(0,len(segments)-1,1):
        new_x=segments[seg_num+1].xcor()
        new_y=segments[seg_num+1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[len(segments)-1].forward(20)
    segments[len(segments)-1].left(random.choice([90,180,270,0]))

screen.exitonclick()