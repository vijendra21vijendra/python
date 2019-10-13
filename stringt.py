"""here we will learn
about strings
"""
x = "vijendra"
"""
slicing of strings
x = "vijendra"
print(x[0:3]) => vij
x[:5] => vijen 
x[:] => x
x[3:1:-1] => ej
x[-5:-2] => end  -5 + 8 to -2 + 8
x[::-1] => reverse of string 
x[::-2] => reverse and then one skip
x[3:1] => doesn't gives because it can go from forward only
we can't acces out of bound directly but when in range it returns in bound things

means that starts from first and don't include last 
"""
# print(x[-5:-2])

"""
Here we will talk about some of string functions
name.isalnum() => false because it contains spaces also
isalpha()
isnumeric()
endswith(val)
.count(val)
.capatialize() => changes first letter to upper case
.find(val) => returns index when first time found
.lower() > lower case 
.upper() > upper case
.replace(a,b) > replace a with b and returns 
"""
name = "vijendra singh Shekhawat"
age = "20"
mystr = "I am a good boy"
# print(name.isalnum())
# print(name.isalpha())
# print(age.isnumeric())
# print(mystr.endswith("boy"))
# print(mystr.count('am'))
# print(name.capitalize())
# print(mystr.find("am"))
# print(name)
# name = name.upper()
# print(name)
# print(name.lower())
# print(mystr.replace("am", "are"))
# print(mystr)

# one problem

x = "my name are lavoareksi shekhawat"
""" here we want to replace are with is """
# x = x.replace("are", "is")
# print(x)

x = x.replace(" are ", " is ")
print(x)

