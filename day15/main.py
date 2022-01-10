
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

drink = input("what would you like ? (espresso/latte/cappuccino) : ")
print(MENU[drink]['cost'])

print("please insert coins")
quarters = int(input("how many quarters ? "))
dimes = int(input("how many dimes ? "))
nickles = int(input("how many nickles ? "))
pennies = int(input("how many pennies ? "))

total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01,2)

print(total)

change = total - MENU[drink]['cost']
print(f"here is your change {change}")

