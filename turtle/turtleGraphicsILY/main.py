import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(500, 500)

tim = Turtle()
tim.color("red")
tim.width(10)
screen.bgcolor("misty rose")

tim.hideturtle()
tim.penup()
tim.goto(-700, 300)
tim.pendown()
tim.showturtle()


def i():
    tim.forward(80)
    tim.right(180)
    tim.forward(40)
    tim.left(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(40)
    tim.right(180)
    tim.forward(80)

def l():
    tim.forward(100)
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def o():
    tim.right(90)
    tim.penup()
    tim.forward(25)
    tim.pendown()
    tim.circle(25, -180)
    tim.right(180)
    tim.forward(50)
    tim.right(180)
    tim.circle(25, -180)
    tim.right(180)
    tim.forward(50)
    tim.penup()
    tim.right(90)
    tim.forward(55)
    tim.left(90)
    tim.forward(25)
    tim.right(90)

def v():
    tim.right(70)
    tim.forward(110)
    tim.left(140)
    tim.forward(110)
    tim.right(70)

def e():
    tim.forward(50)
    tim.left(180)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(180)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def y():
    tim.forward(50)
    tim.left(120)
    tim.forward(50)
    tim.left(120)
    tim.left(60)
    tim.forward(50)
    tim.left(30)
    tim.forward(50)
    tim.left(90)

def u():
    tim.right(90)
    tim.forward(75)
    tim.circle(25, 180)
    tim.forward(75)


def curve():
    for i in range(200):
        # Defining step by step curve motion
        tim.right(1)
        tim.forward(1)


def heart():
    # Set the fill color to red
    tim.fillcolor('red')

    # Start filling the color
    tim.begin_fill()

    # Draw the left line
    tim.left(140)
    tim.forward(113)

    # Draw the left curve
    curve()
    tim.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    tim.forward(112)

    # Ending the filling of the color
    tim.end_fill()
def fn():
    i()
    tim.penup()
    tim.left(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.pendown()
    l()
    tim.penup()
    tim.forward(100)
    tim.right(90)
    tim.forward(10)
    tim.pendown()
    o()
    tim.penup()
    tim.forward(10)
    tim.pendown()
    v()
    tim.penup()
    tim.forward(10)
    tim.pendown()
    e()
    tim.penup()
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(60)
    tim.pendown()
    y()
    tim.penup()
    tim.forward(38)
    tim.left(90)
    tim.forward(100)
    tim.right(90)
    tim.pendown()
    o()
    tim.penup()
    tim.forward(10)
    tim.pendown()
    u()
    tim.right(90)

fn()
tim.hideturtle()
tim.penup()
tim.goto(300, 100)
tim.pendown()
tim.showturtle()
heart()

screen.exitonclick()