""" in includes functions and docstrings """
#
# a = 3
# c = 53
# b = (a, c)
# print(sum(b))
#
# print(sum.__doc__)


def average(a,b):
    """this is average and returns floor of two nums average"""
    return (a+b)//2
def noret():
    print("what is this")
    """this is a comment not a doc strings because doc string is starting of function"""
# print(average(4,7))
# print(average.__doc__)
print(noret())
print(noret.__doc__)