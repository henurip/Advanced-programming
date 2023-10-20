def calculateTotal(amount, discountPercentage = 0):
    discountAmount = discountPercentage / 100 * amount
    return amount - discountAmount

def fun(a=0,b=0,c=0):
    print("a = " , a)
    print("b = " , b)
    print("c = " , c)

fun(c = 5,b=2,c=3)

amount = 500
totalBillAmount = calculateTotal(amount, 10)
print(totalBillAmount)

account = 500
totalBillAmount = calculateTotal(amount)
print(totalBillAmount)
