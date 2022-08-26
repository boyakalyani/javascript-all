from socket import if_nameindex

cost_price=int(input("enter the number "))
selling_price=int(input("enter the nmumber"))
a=cost_price-selling_price
if cost_price>selling_price:
    print("profit of" ,a, "rs")
elif cost_price<selling_price:
    print("loss of" ,a, "rs")
else:
    print("no profit no loss")

