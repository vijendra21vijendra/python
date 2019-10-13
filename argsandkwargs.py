
""" this is fine
noraml :> string
*args :> tuple
*kwargs :> dict

"""
# def printer(name):
#     print(name)
#     name[1] = "ramu"
#
#
#
# x = ["rakesh", "suresh", "harimohan"]
# print(x)
# printer(x)
# print(x)





def func(normal, *args, **kwargs):
    print(type(normal), type(args), type(kwargs))
    print(normal)
    for val in args:
        print(val)
    for key, pair in kwargs.items():
        print(key, pair)


normal = "i am here: "
names = ["rakesh", "ram", "shyam"]
workand = {
    "rakesh":112,
    "shyam":"sona"
}
func(normal, *names, **workand)










