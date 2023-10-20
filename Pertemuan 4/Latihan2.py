def mysum(*a):
    total = 0
    for ele in a:
        print(total,"+",ele,"=",end=' ')
        total += ele #total=total+ele
        print(total)
    return total

print(mysum(5,2,9,4))