# def format_name(first_name,last_name):
#     if first_name == "" or last_name == "":
#         return "wrong"
#     formated_f_name = first_name.title()
#     formated_l_name = last_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("what is your first name?"),input("what is your last name?")))


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input( "Enter a year: " ) )
# month = int ( input ( "Enter a month: " ) )
# days = days_in_month (year, month)
# print ( days )


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b


dict_1 = {
     "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# print(len(dict_1))
def calculator():
    num1 = float(input("what is the first number ?"))
    # 两种方法都可以for symbol in dict_1.keys():
    for symbol in dict_1:
        print(symbol)


    end_of_game = False
    while not end_of_game:
        operation_symbol = input ( "pick an operation:" )
        # print(operation_symbol)

        num2 = float(input("what is the next number ?"))

        answer = dict_1[operation_symbol] ( num1, num2 )
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        go_on = input(f"type 'y' to continue with {answer} or type 'n' to a new start.")

        if go_on == "y":
            end_of_game = False
            num1 = answer
        elif go_on == "n":
            end_of_game = True
            calculator()

calculator()
# 我是最棒的







