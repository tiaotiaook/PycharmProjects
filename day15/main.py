
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

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry ,there is not enough {item}")
            return False
    return True


def coins():
    print ( "please insert coins" )
    total = int(input("how many quarters ? ")) * 0.25
    total += int(input("how many dimes ? ")) * 0.1
    total += int(input("how many nickles ? ")) * 0.05
    total += int(input("how many pennies ? ")) * 0.01
    return total

def enough_money(money_received,drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True

while is_on:
    choice = input("what would you like ? (espresso/latte/cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}" )
        print(f"coffee : {resources['coffee']}")
        print(f"money : {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = coins()
            if enough_money(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])













#
# def money():
#     print("please insert coins")
#     quarters = int(input("how many quarters ? "))
#     dimes = int(input("how many dimes ? "))
#     nickles = int(input("how many nickles ? "))
#     pennies = int(input("how many pennies ? "))
#
#     total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01,2)
#
#     print(total)
#
#     change = total - MENU[drink]['cost']
#     print(f"here is your change {change}")
#
#
# def last(drink):
#
#     water_last = resources['water'] - MENU[drink]['ingredients']['water']
#     print(f"water last {water_last}")
#     milk_last = resources['milk'] - MENU[drink]['ingredients']['milk']
#     print(f"milk last {milk_last}")
#     coffee_last = resources['coffee'] - MENU[drink]['ingredients']['coffee']
#     print(f"coffee last {coffee_last}")
#
#
# go_on = True
# while go_on:
#     drink = input("what would you like ? (espresso/latte/cappuccino) : ")
#     print(MENU[drink]['cost'])
#     if drink == "off":
#         go_on = False
#     elif drink == "report":
#
#
#
#     last(drink)
#
#     # if water_last < MENU[drink]['ingredients']['water'] or milk_last < MENU[drink]['ingredients']['milk'] or coffee_last < MENU[drink]['ingredients']['coffee']:
#     #     print("sorry")
#
#     money()