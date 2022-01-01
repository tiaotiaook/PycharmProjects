# from turtle import Turtle,Screen
# timmy = Turtle()
# # timmy object  Turtle() class
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squitle","Charmander"])
table.add_column("Pokemon Type",["electric","water","fire"])
table.align = "l"
print(table)