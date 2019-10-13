""" here we will talk about fstrings and formatting of the strings
1. Fstrings    a = f"my name is {name} and i am from {village}"



 """
name = "vijendra singh"
village = "kumas jagir"
# a = f"my name is {name} and i am from {village} and i am {15+5} years old"
# print(a)

a = " my name is %s and i am from %s"%(name,village)
print(a)

a = "this is {1} and he is from {0}"
b = a.format(village, name)
print(a, b)
