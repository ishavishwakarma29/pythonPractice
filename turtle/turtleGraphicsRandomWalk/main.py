import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(500, 500)

tim = Turtle()
turtle.colormode(255)
screen.bgcolor("black")
def color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


directions = [0, 90, 180, 270]
tim.width(8)
tim.speed("fastest")

while True:
    tim.color(color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
