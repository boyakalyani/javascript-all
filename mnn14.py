i=1
s=0
while i<=11:
     n=int(input("enter weight"))
     s=s+n
     avrg=s//11
     i=i+1
print(avrg)
if avrg%5==0:
     print("Yes,divisible")
else:
    print("not divisible")


i=0
s=0
while i<=11:
     a=int(input("ente weight"))
     s=s+a
     avrg=s//11
     i+=1
print(avrg)
if i%5==0:
     print("divisebe")
else:
     print("not")