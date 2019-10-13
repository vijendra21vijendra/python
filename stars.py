num = int(input("enter a num: "))
boolval = bool(input("enter a bool val"))
a = b = None
if boolval == True:
    a=0
    b=1
else:
    a=num-1
    b=-1
for x in range(num):
    i=0
    while i<=a:
        print("* ",end="")
        i+=1
    a+=b
    print()