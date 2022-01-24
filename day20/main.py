
from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)


# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)

starting_position = [(0,0),(-20,0),(-40,0)]

segment_list = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment_list.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segment_list:
        seg.forward(20)











screen.exitonclick()