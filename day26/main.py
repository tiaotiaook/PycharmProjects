numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

# new_list = [new_item for item in list]

name = "Angela"
new_list  = [letter for letter in name]
print(new_list)

new_number = [ 2*num  for num in range(1,5)]
print(new_number)

# new_list = [new_item for item in list if test]

names = ["jsgd","suigdu","shd","shgdkbcjkw","sjgc","hs","hfhhj"]
# short_names = [name for name in names if len(name)<5 ]
# print(short_names)
long_names = [name.upper() for name in names if len(name)>5]
print(long_names)