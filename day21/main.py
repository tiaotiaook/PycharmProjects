class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this under water.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


# from turtle import Turtle,Screen
# screen = Screen()
# tim = Turtle()
# tim.shape("square")
# tim.pensize(100)
# tim.goto(x=-230, y=0)


screen.exitonclick()