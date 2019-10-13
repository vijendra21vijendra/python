import time
#
# initialtime = time.time()
# print(initialtime)
# for i in range(10000000):
#     i+=1
#
# timenow = time.time()
# print(timenow)
# print(timenow-initialtime)

localtime = time.asctime(time.localtime(time.time()))
print(type(localtime))
time.sleep(3)
print(localtime)