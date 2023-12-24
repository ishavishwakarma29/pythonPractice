import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(500, 500)

tim = Turtle()
tim.color("red")
screen.bgcolor("black")

color = ["yellow", "red", "blue", "green", "pink", "purple", "orange", "misty rose"]
angle = [120, 90, 72, 60, 360/7, 45, 40, 36]

for i in range(0, 8):
    tim.color(color[i])
    for j in range(0, 3+i):
        tim.right(angle[i])
        tim.forward(100)

screen.exitonclick()