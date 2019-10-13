""" try except and finally are the world """


num1 = input("enter a num\n")
num2 = input("enter another num\n")
try:
    print("sum is", int(num1)+int(num2))
except Exception as e:
    print(e)
finally:
    print("this is executed everytime ")
print("I am fine")
