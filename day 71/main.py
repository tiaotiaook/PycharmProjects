import pandas as pd

# pd_reader = pd.read_csv("salaries_by_college_major.csv")
#
# print(pd_reader)


with open("salaries_by_college_major.csv") as f:
    for line in f:
        print(line)
