import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
mikki = turtle.Turtle()
mikki.speed(20)
mikki.color("blue")
side=5
mikki.penup()
mikki.goto(0,0)
mikki.pendown()
mikki.pensize(3)

for i in range (91):
    mikki.forward(side)
    mikki.left(91)
    side=side+5


mikki.penup()
mikki.goto(500,500)