""" this is another method af opening and closing files togethere """
# f.readlines() just returns a list of data as strings
# with open("viju.txt") as f:
#     print(f.readlines())

f = open("vijubanna.txt", "a")
print(f.write("how are you dear\n"))