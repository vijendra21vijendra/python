def fac(n):
    # return n*fac(n-1)# gives error
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

print(fac(5))