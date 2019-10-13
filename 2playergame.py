"""this is game for 2 player"""
import random
chars = ["snake", "water", "gun"]
while True:
    print(chars)
    x = input("choose on of this\n")
    myvar = random.choice(chars)
    res = None
    if x == myvar:
        res = "match Tie"
    elif x == "snake":
        if myvar == "water":
            res = f"you won cuz mine was {myvar} "
        else:
            res = f"you lost cuz mine was {myvar}"
    elif x == "water":
        if myvar == "gun":
            res = f"you won cuz mine was {myvar} "
        else:
            res = f"you lost cuz mine was {myvar}"
    elif x == "gun":
        if myvar == "snake":
            res = f"you won cuz mine was {myvar} "
        else:
            res = f"you lost cuz mine was {myvar}"
    print(res)
    a = input("enter 1 for exit()\n")
    if a == "1":
        break
