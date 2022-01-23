from turtle import Turtle, Screen
import random
go_on = True
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make a bet",prompt="which color will win?")
colors = ["red","orange","yellow","green","blue","purple"]
y = [-70,-40,-10,20,50,80]
all_turtle = []

for turtle_index in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230,y=y[turtle_index])
    all_turtle.append(timmy)


if user_bet:
    go_on = True

while go_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            go_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win, the {user_bet} is the winner.")
            else:
                print("you lose, the {user_bet} is the winner.")



        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()