"""lambda function are just anonymous functon"""

add = lambda x, y: x+y
minus  = lambda x, y: x-y
mult = lambda a, b: a*b
#
#
# print(add(75,4))
# print(mult(34,9))
# print(minus(1,23))

asa =[[2,23],[15,12],[8,17]]
a = asa.copy()
a.sort(key=lambda x:x[1])
print(a)
print(asa)