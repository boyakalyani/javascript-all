a=int(input("enter the bike cost price"))
if a>100000:
    print("road tax",15/100)
elif a>50000 and a<=100000:
    print("road tax",10/100)
elif a<=50000:
    print("road tax",5/100)
else:
    print("no road tax")
