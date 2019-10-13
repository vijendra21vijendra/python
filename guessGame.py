"""this is a guess game and you have x chances """
import random
print("\t\t\t\t*******Guess Game*****\n\n")
a = int(input("enter how many chances you want\n"))
secret_num = random.randrange(100)
while a > 0:
    val = int(input("enter your guess\n"))
    if val==secret_num:
        print("successful")
        break
    elif val>secret_num:
        print("you entered more lessen it")
    else:
        print("you entered less increase it")
    a-=1
if a==0:
    print("game over you lost")
    print(secret_num, " was the number")
