
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

color_list = [[245, 243, 238], [246, 242, 244], [202, 164, 110], [240, 245, 241], [236, 239, 243], [149, 75, 50],
              [222, 201, 136], [53, 93, 123], [170, 154, 41], [138, 31, 20], [134, 163, 184], [197, 92, 73],
              [47, 121, 86], [73, 43, 35], [145, 178, 149], [14, 98, 70], [232, 176, 165], [160, 142, 158],
              [54, 45, 50], [101, 75, 77], [183, 205, 171], [36, 60, 74], [19, 86, 89], [82, 148, 129], [147, 17, 19],
              [27, 68, 102], [12, 70, 64], [107, 127, 153], [176, 192, 208], [168, 99, 102]]



timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

timmy.hideturtle()

timmy.penup()

timmy.setx(-300)
timmy.sety(-300)


for n in range(1,101):

    timmy.dot(10,random.choice(color_list))
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()

    if n % 10 == 0:
        timmy.penup()
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)








screen = Screen()
screen.exitonclick()