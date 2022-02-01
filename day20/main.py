
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    if snake.head.xcor() > 295 or snake.head.xcor() < -295 \
            or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment in snake.segments:
            pass
        elif snake.heading.distance(segment)<10:
            scoreboard.reset()
            snake.reset()














screen.exitonclick()




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