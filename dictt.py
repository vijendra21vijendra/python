""" this is dictionary
and it is mutable
and pointed
key value pairs are here keys should be unique and values can be anything
keys: nums and strings

function on dictionaries
 del d[key]
 .update({}) adds if not found otherwise updates
 .get(key)
 .keys
 .items()

"""

# d1 = {}
# print(type(d1))
d2 = {
    "vijendra":"chicken",
    "ram":"roti",
    45:"kebabs",
    "hari":"sweets"
}
print(d2)
# del d2[45]
# d2["amit"] = "eggs bhurji"
# d2["zen"] = {
#     "B":"apples",
#     "L":"pizzas",
#     "D":["ghas", "phus"]
# }
# print(d2["amit"])
# print(d2["zen"]["D"][1])
# print(d2)
# m = d2.keys()
# print(m)
# print(d2.items())
# print(d2.get(45))

d2.update({1:"shyama"})
d2[45] = "rice"
print(d2)
d2.update({1:"rama"})
print(len(d2))

