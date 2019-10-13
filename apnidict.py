"""this is my dictionary where there are some meanings """

print("\t\t\t****Apni Dictionary***\n\n\n")
mydict = {
    "president":"Ram Nath Kovind",
    "prime minister":"Narendra Modi",
    "chief Minister":"Ashok Gehlot",
    "warrior":"Rajputs",
    "King":"Rajputs of rajasthan"
}
keys = list(mydict.keys())
while True:
    print(keys)
    key = input("enter a key: ")
    print("answer is ", mydict[key])
    a = input("enter x and come out: ")
    if a=="x":
        break

