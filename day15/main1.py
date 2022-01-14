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

def enough_ingredients(choice_need):
    for item in choice_need:
        if choice_need[item] > resources[item]:
            print(f"sorry not enough {choice_need[item]}")
            return False
        return True


def should_pay():
    print("please insert coins")
    total = int(input("how many quarters ? ")) * 0.25
    total += int(input("how many dimes ? ")) * 0.1
    total += int(input("how many nickles ? ")) * 0.05
    total += int(input("how many pennies ? ")) * 0.01
    return total


def enough_money(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost ,2)
        return True
    else:
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print ( f"here is your {drink_name}" )



is_on = True
while is_on:

    choice = input("what would you like ? (espresso/latte/cappuccino) :")


    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water last: {resources['water']}")
        print(f"milk last: {resources['milk']}")
        print(f"coffee last: {resources['coffee']}")
    else:
        # 判断剩余材料够不够

        choice_need = MENU[choice]['ingredients']
        print(choice_need)
        if enough_ingredients(choice_need):
            payment = should_pay()
            if enough_money(payment,MENU[choice]['cost']):
                make_coffee(choice,MENU[choice]['ingredients'])







