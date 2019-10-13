""" this is for file writing and file appending

"""
#f.write returns the no of characters it writes
# f = open("a.txt", "w")
# f.write("i am the king of this universe\n")
# print(f.write("how are you\n"))
# f.write("what are you doing\n")
#
# f = open("a.txt", "a")
# p = f.write("this is the thing which is appended in the file\n")
# print(p)
# f.write("and this is second line\n")


# it is same like pointers
# this mode is for update file
#f = open("a.txt", "r+")
# print(f.read(8))
# print(f.read())
#f.close()


""" there is some confusion when open in update that 
when you directly start write then it writes from first position
and if you first have read one character only then after it will write in 
the end of file 
and one more thing is that what have you written just now don't reflect in the read mode
"""

f = open("a.txt", "r+")
print(f.read(1))
# now i want to write something but it will wtitten in the end
print(f.tell())
f.write("yes what is this man\n")
print(f.tell())
f.seek(0)
print(f.read())