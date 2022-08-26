# i=1
# counter=0
# a=int(input("entr"))
# while i<=a:
#     if a%i==0:
#         counter+=1
#     i+=1
# if counter==2:
#     print("prime")
# else:
#     print("not prime")



i=1
a=int(input("enter"))
f=0
while i<=a:
    if a%i==0:
        f+=1
    i+=1
if f==2:
    print("prime")
else:
    print("not prime")