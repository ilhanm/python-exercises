from turtle import Screen,Turtle
DOWN=270
UP=90
LEFT=180
RIGHT=0
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[len(self.segments)-1]
    def create_snake(self):
        for i in range(5):
            newSegment=Turtle()
            newSegment.penup()
            newSegment.color("white")
            newSegment.shape('square')
            newSegment.setx(i*20)
            self.segments.append(newSegment)
    
    def move(self):
        for seg_num in range(0,len(self.segments)-1,1):
            new_x=self.segments[seg_num+1].xcor()
            new_y=self.segments[seg_num+1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[len(self.segments)-1].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
 
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)