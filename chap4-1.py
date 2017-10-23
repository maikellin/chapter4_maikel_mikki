import turtle

def make_square(turt,size,num):
    for j in range(num):
        turt.pendown()
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.penup()
        turt.forward(2*size)
        
wn=turtle.Screen()
name=turtle.Turtle()
wn.bgcolor("lightgreen")
name.color("hotpink")
name.pensize(3)

        
make_square(name,20,5)
