print("welcome to the the tip calculator.")
bill = float(input("what is the total bill ? \n"))
people = int(input("how many people to split the bill ?\n"))
percentage = int(input("what percentage tip would you like to give ? 10,12 or 15 ?\n"))
should_pay = float(
    (bill * (1 + percentage/100 ))/5

     )
# print(should_pay)
print(f"each person should pay :${should_pay}" )

# print("Hello"[4])