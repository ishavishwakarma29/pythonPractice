import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(500, 500)

tim = Turtle()
turtle.colormode(255)
def color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim.speed("fastest")


def draw(size):
    for i in range(0, 360//size):
        tim.color(color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size)


draw(5)
screen.exitonclick()