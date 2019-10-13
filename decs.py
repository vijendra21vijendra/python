"""this is the file which tells about the decoraters

"""
# here we can see that after deletion also we can execute means a copy of function is created
# def function():
#     print("how are you")
#
# func1 = function
# del function
# func1()

def func1(func):
    def func2():
        print("i am about to start execution")
        func()
        print("i have completed")
    return func2

# def func():
#     print("adding")
#
# func = func1(func)
# func()

# and another way of doing is
@func1
def func():
    print("adding")

func()
