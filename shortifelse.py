""" one liner for if and else """
a = int(input("enter num\n"))
b = int(input("enter other num\n"))
# if a>b: print("a is greater then b")
# print("a is greater then b") if a>b else print("a is lesser or equal to b")


print("a is equal to b") if a==b else print("a is greater then b") if a>b else print("a is lesser then b")