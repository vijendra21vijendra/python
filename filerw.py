"""
this is for file reading and writing
"r" :> open file in read mode by default also it opens in read mode can use :: rt for read text and rb for read binary
"w" :> in write mode
"x" :> creates file if not exists
"a: :> for appending the data
"t" :> text mode
"b" :> binary mode
"+" :>>> for read and write both means updating

functions
fptr = open("path",mode)
content = fptr.read()
fptr.readline()
fptr.readlines()
let file is viju.txt
"""

f = open("viju.txt")
#f = open("viju.txt", "rb")
content = f.read()
# content = f.read(3)
print(content)
#print(f.readlines()) #returns a list
# x = f.readlines()
# for line in x:
#     print(line,end="")

# for line in f:
#     print(line,end="")

# for x in content:
#     print(x,end="1")
f.close()