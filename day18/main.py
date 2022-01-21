import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# fangxiang = [0,90,180,270]
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")


# timmy_the_turtle.color("red")

# for n in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# for n in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# side = int(input("how many side you want?"))



# def draw(side):
#     timmy_the_turtle.color(random.choice(colors))
#     jiao = 360 / side
#     for n in range(side):
#         timmy_the_turtle.right(jiao)
#         timmy_the_turtle.forward(100)
#
#
# for n in range(3,11):
#     draw(n)

def colo():
    r = random.randint(0,255)
    g = random.randint ( 0, 255 )
    b = random.randint ( 0, 255 )
    color = (r,g,b)
    return color

# def run():
#     timmy_the_turtle.color (colo() )
#     timmy_the_turtle.forward ( 30 )
#     timmy_the_turtle.setheading(random.choice ( fangxiang ))
#
# for n in range(200):
#     run()

def draw(size):
    for n in range(int(360 / size)):
        timmy_the_turtle.color(colo())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + 1)


draw(1)

screen = Screen()
screen.exitonclick()
