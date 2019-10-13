"""here we see about the scope of the vars and
global keyword is for only fully global vars
"""

# a = 5
# def func():
#     # you have to specify in function that var is global or local both can't work
#     #print(a)
#     #a = 23
#     global a
#     a += 12
#     print(a)
#
# func()
# print(a)

def ram():
    x = 23
    def shyam():
        global x
        x = 32
        print(x)
    print(x)
    shyam()
    print(x)
ram()
print(x)