
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def money():
    print("please insert coins")
    quarters = int(input("how many quarters ? "))
    dimes = int(input("how many dimes ? "))
    nickles = int(input("how many nickles ? "))
    pennies = int(input("how many pennies ? "))

    total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01,2)

    print(total)

    change = total - MENU[drink]['cost']
    print(f"here is your change {change}")


def last(drink):

    water_last = resources['water'] - MENU[drink]['ingredients']['water']
    print(f"water last {water_last}")
    milk_last = resources['milk'] - MENU[drink]['ingredients']['milk']
    print(f"milk last {milk_last}")
    coffee_last = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    print(f"coffee last {coffee_last}")


go_on = False
while not go_on:
    drink = input("what would you like ? (espresso/latte/cappuccino) : ")
    print(MENU[drink]['cost'])

    last(drink)

    # if water_last < MENU[drink]['ingredients']['water'] or milk_last < MENU[drink]['ingredients']['milk'] or coffee_last < MENU[drink]['ingredients']['coffee']:
    #     print("sorry")

    money()