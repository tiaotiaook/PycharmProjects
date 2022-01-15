# import another_module
# print(another_module.another)


# import turtle
#
# timmy = turtle.Turtle()

# from turtle import Turtle,Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# Screen().exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("city name",["beijing","shanghai","tianjin"])
table.add_column("city like",["lala","bibi","jiji"])
table.align = "l"
print(table)



