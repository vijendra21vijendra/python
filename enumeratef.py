"""here we will talk about when to use enumerate and how to use it
"""

#names = [["vijendra", "singh"], ["shekhawat", "kumas Jagir"]]
names = ["vijendra", "singh", "shekhawat", "kumas Jagir"]

for index, val in enumerate(names):
    print(type(index),type(val))
    print(f"names[{index}] = {val}")