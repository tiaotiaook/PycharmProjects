MENU = {
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18, }, "cost": 1.5, },
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0, }
}
# print(MENU["latte"]["cost"])
profit = 0
# 利润
resources = {"water": 300, "milk": 200, "coffee": 100, }
#
# coffee = input("what would you like ? (espresso/latte/cappuccino): ")
# print("Please insert coins.")
#
# quarters = float(input("how many quarters?:")) * 0.25
# dimes = float(input("how many dimes?:")) * 0.1
# nickles = float(input("how many nickles?:")) * 0.05
# pennies = float(input("how many pennies?:")) * 0.01
#
# total = quarters + dimes + nickles + pennies
# print(round(total, 2))
# change = total - MENU[str(coffee)]["cost"]
# print(round(change, 2))
#
# report = {
#     "water": resources["water"] - MENU[str(coffee)]["ingredients"]["water"],
#     "milk": resources["milk"] - MENU[str(coffee)]["ingredients"]["milk"],
#     "coffee": resources["coffee"] - MENU[str(coffee)]["ingredients"]["coffee"],
# }
# print(report)

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money.")
        return False





def process_coins():
    print("please insert coins. ")
    total = float(input("how many quarters?:")) * 0.25
    total += float(input("how many dimes?:")) * 0.1
    total += float(input("how many nickles?:")) * 0.05
    total += float(input("how many pennies?:")) * 0.01
    return total

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}. ")

is_on = True

while is_on:
    choice = input("what would you like ? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])











