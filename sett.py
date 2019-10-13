""" there is a set type also in the pythonn"""


# s = set()
# s.add(5)
# s.add("ram")
# s.add(1)
# print(s)
# s.remove("ram")
# print(s)

""" set using list """
name = ["vijendra", "ram", "shyam", "radha"]
s = set(name)
print(s)
s1 = set(["geeta", "sita", "ram"])
print(s1)
print(len(s1), max(s1), min(s1))
r = s.union(s1)
print(r)
r = s1.intersection(s)
print(s1.isdisjoint(s))
s.clear()
s1.clear()