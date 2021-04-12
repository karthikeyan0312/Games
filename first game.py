import turtle
import winsound
wn=turtle.Screen()
wn.title("my first game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#paddle A
pad1=turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.shapesize(stretch_wid=5,stretch_len=1)
pad1.penup()
pad1.goto(-350,0)

#paddle B
pad2=turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("blue")
pad2.shapesize(stretch_wid=5,stretch_len=1)
pad2.penup()
pad2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=0.89
ball.dy=-0.89

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A:0  player B:0",align="center",font=("courier",24,"normal"))
 #score
sa=0
sb=0




#function
#move up
def pad1_up():
    y=pad1.ycor()
    y+=20
    pad1.sety(y)
#move down
def pad1_down():
    y=pad1.ycor()
    y-=20
    pad1.sety(y)
def pad2_up():
    y=pad2.ycor()
    y+=20
    pad2.sety(y)
#move down
def pad2_down():
    y=pad2.ycor()
    y-=20
    pad2.sety(y) 




wn.listen()
#for pad1
wn.onkeypress(pad1_up,"a")
wn.onkeypress(pad1_down,"s")
#for pad2
wn.onkeypress(pad2_up,"k")
wn.onkeypress(pad2_down,"l")



while True:
    wn.update()
    #winsound.PlaySound('Evil Ambiance.wav',winsound.SND_ASYNC)
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #bounce ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -0.89
        #SND_FILENAME
        winsound.PlaySound('Water Balloon.wav',winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -0.89
        winsound.PlaySound('Water Balloon.wav',winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-0.89
        sa+=1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(sa,sb),align="center",font=("courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-0.89
        sb+=1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(sa,sb),align="center",font=("courier",24,"normal"))

#paddle and ball collide
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()< pad2.ycor()+40 and ball.ycor() > pad2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() <-340 and ball.xcor()>-350) and (ball.ycor()< pad1.ycor()+40 and ball.ycor() > pad1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

