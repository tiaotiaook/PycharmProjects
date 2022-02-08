def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)



add(3,5,6,4,5,7,5,4,6,8,34,65)


def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)




calculate(2,add = 3,multiply = 5)



class Car:
    def __init__(self,**kw):
        self.made = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("seats")


my_car = Car(model = "gtr",made = "nissan")
print(my_car.made)