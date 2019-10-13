""" this is a faulty calc which
performs all operation right except these
1. 45*3 = 555
2. 56 + 9 = 77
3. 56/6 = 4
"""
print("\t\t\t\t****calculator****\n\n")
operator = input("enter operator: ")
op1 = int(input("enter first operand: "))
op2 = int(input("enter second Operand: "))
val = None
if op1==45 and op2 == 3 and operator=="*":
    val = 555
elif op1==56 and op2==9 and operator=="+":
    val = 77
elif op1 == 56 and op2==6 and operator=="/":
    val = 4
else:
    if operator=="+":
        val = op1 + op2
    elif operator=="-":
        val = op1 - op2
    elif operator=="*":
        val = op1* op2
    elif operator == "/":
        val = op1/op2
    elif operator=="%":
        val = op1%op2
    elif operator=="^":
        val = op1^op2
    elif operator=="&":
        val = op1&op2
    else:
        val = "Galat input"
print(val)
