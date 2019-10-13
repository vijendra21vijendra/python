"""here is how continue and break statement used
break means just break the loop where you are
continue: means just return from where you have gone and start for another value of loop


"""
#
# i=1
# while True:
#     if i<10:
#         i+=1
#         continue
#     elif i>50:
#         break
#     print(i)
#     i+=1

""" exercise take input until value is not more than 100 """
while True:
    a = input("enter the value:\n")
    if int(a)>=100:
        break
    print("try again")
print("successful person")

