""" here we will study for loop """

a = [1, 2, 3, 432, 5, 89, "rani"]
# for item in a:
#     print(item)
#
# for val in a:
#     if str(val).isnumeric() and val>30:
#         print(val)

b = [["ram", 3],["shyam", 5],["rakesh", 35]]

# for name,val in b:
#     print(name, " eats ",val,"chapatis")

# b = [["ram", 3,89],["shyam", 5,8909],["rakesh", 35,567]]
#
# for items in b:
#     for x in items:
#         print(x, end=" ")
#     print()

dic = dict(b)
for name,val in dic.items():
    print(name,val)