def mymax(a,*b):
    large = a
    for ele in b:
        if ele>large:
            large = ele
    return large

print(mymax(9,5,7,3,1,8,2))