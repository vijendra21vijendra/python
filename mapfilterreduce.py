"""
here we will learn about map function
map takes input as a function and a iterable
a = list(map(func,list))
map returns object and we convert it into list
"""

#nums = [1, 4, 5, 2, 11, 8]
# sqr = list(map(lambda x: x*x,nums))
# print(sqr)
#
# def sqr(a):
#     return a*a

# def cube(a):
#     return a*a*a
#
# def power(a):
#     return a**a
# lis = [sqr,cube,power]
#
# for i in range(10):
#     p = list(map(lambda x: x(i+1), lis))
#     print(p)


""" filter  function now here

it just filters the iteratable on the basis of the provided function
"""

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_odd_and_gt_4(num):
#     if num%2==1 and num>4:
#         return True
#     else:
#         return False
#
#
# print(nums)
# x = list(filter(is_odd_and_gt_4, nums))
# print(x)


"""reduce function uses and how to do
from functools import reduce
num = reduce(func,list)
> returns a value means reduces in the one value
"""
# import time
from functools import reduce
lis = [1, 5, 23, 6]
# ini = time.time()
# sum = 0
# for val in lis:
#     sum += val
# print(sum)
# print(time.time()-ini)
# ini = time.time()
num = reduce(lambda x,y : x+y,lis)
print(num)
# print(time.time()-ini)

