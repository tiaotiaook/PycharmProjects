def add(*args):
    print(args[0])
    sum = 10003
    for n in args:
        sum -= n
    return sum

# print(add(1,2,3,4,5,6,3,5,8,9,3,5,6,4,5,6,788))



def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
#     2+3=5 5*5=25


calculate(2,add=3,multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make = "nissan")
print(my_car.model)
