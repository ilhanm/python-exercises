from turtle import Turtle, Screen
screen= Screen()
rıfkı=Turtle()
rıfkı.shape("turtle")
rıfkı.color('navyblue', 'brown')
def drawStar():
    rıfkı.color('navyblue', 'yellow')
    rıfkı.speed(10)
    rıfkı.begin_fill()
    while True:
        rıfkı.forward(200)
        rıfkı.left(170)
        if abs(rıfkı.pos()) < 1:
            break
    rıfkı.end_fill()    
rıfkı.speed(10)            
def weirdoshape():
    for j in range(4):
        rıfkı.left(90)
        for i in range(10):
            rıfkı.begin_fill()
            rıfkı.circle(5+i*5)
            rıfkı.end_fill()
            rıfkı.forward(10)
        rıfkı.backward(100)

mybool=True

rıfkı.home();rıfkı.clear()
for i in range(200):
        rıfkı.forward(i)
        rıfkı.circle(150+i,25)
        rıfkı.left(90)



screen.exitonclick()


