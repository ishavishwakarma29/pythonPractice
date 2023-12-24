import random
from turtle import Turtle, Screen


screen=Screen()
screen.setup(500, 400)

inp = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
color = ["red", "blue", "green", "orange", "yellow", "purple"]
curr=0

turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230, y=-120+curr)
    turtles.append(tim)
    curr+=50

flag = False

if inp:
    flag= True

while flag:
    for turtle in turtles:
        if turtle.xcor() > 230:
           winning_color = turtle.pencolor()
           tim=Turtle()
           tim.pencolor("black")
           tim.hideturtle()
           tim.penup()
           tim.goto(-200, 0)
           if winning_color == inp:
               tim.write(f"You won {winning_color} is the winner", font = ("Arial", 18, "italic"))
           else :
               tim.write(f"You lost {winning_color} is the winner", font = ("Arial", 18, "italic"))
           flag=False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
