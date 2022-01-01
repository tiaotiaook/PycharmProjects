# from turtle import Turtle,Screen
#
# timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("turtle")
# # timmy_the_turtle.shape("square")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

# for i in range (4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)


# import heroes
# print(heroes.gen())
# import turtle
# from turtle import Turtle,Screen
# import random
#
#
# timmy = Turtle()
# turtle.colormode(255)
#
#
#
# def random_color():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    return(r,g,b)
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0,90,180,270]
# timmy.shape("turtle")
#
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#    timmy.color(random_color())
#    timmy.forward(30)
#    timmy.setheading(random.choice(directions))
#
#
#
# # for i in range (15):
# #
# #    timmy.forward(10)
# #    timmy.penup()
# #    timmy.forward(10)
# #    timmy.pendown()
#
# # for i in range (15):
# #    timmy.color("black")
# #    timmy.forward(10)
# #    timmy.color("white")
# #    timmy.forward(10)
#
# screen = Screen()
# screen.exitonclick()


import turtle
from turtle import Turtle,Screen
import random


timmy = Turtle()
turtle.colormode(255)

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return(r,g,b)


timmy.speed("fastest")

def draw_spirograph(size_of_gap):
   for _ in range(int(360 / size_of_gap)):
      timmy.color(random_color())
      timmy.circle(100)
      timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)







screen = Screen()
screen.exitonclick()