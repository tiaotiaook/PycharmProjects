from turtle import Turtle, Screen
import random

colors = ["red","blue","green","yellow"]
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
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



def draw(side):
    timmy_the_turtle.color (random.choice(colors) )
    jiao = 360 / side
    for n in range(side):
        timmy_the_turtle.right(jiao)
        timmy_the_turtle.forward(100)


for n in range(3,11):
    draw(n)










screen = Screen()
screen.exitonclick()
