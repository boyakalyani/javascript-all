from statistics import quantiles


quantity=int(input("enter the quantity"))
discount=(quantity*10/100)
total=(quantity-discount)
if quantity>=1000:
    print(total)
else:
    print("no discount")




    