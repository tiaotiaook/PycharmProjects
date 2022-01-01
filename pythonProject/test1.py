# import math
# def function(number):
#     l = len(str(number))
#     n = int(number)
#     c = 0
#     if n < 0:
#         return "false"
#     elif 0 <= n <= 9:
#         return "true"
#     elif n > 9:
#         for i in range(0, l):
#             a =int((n % math.pow(10, i+1)) / math.pow(10,i))
#             #  4
#             print(a)
#             b = a * math.pow(10, l - 1)
#             # 4000
#             print(b)
#             i += 1
#             l -= 1
#             c = c + b
#             print(c)
#         print(c)
#         if c == n :
#                 return "true"
#         else :
#                 return "false"
#
# number = int(input("what is your number ? : "))
# print(function(number))

print("hello world")
print("hello world"[::-1])
print("hello world"[::-2])
print("hello world"[::-3])