n=int(input("enter"))
a=1
b=0
i=0
while i<n:
    c=a+b
    a=b
    b=c
    print(c)
    i+=1