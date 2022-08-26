i=0
s=1
n=int(input("enter"))
while i<n:
    k=n%10
    n=n//10
    s=s*k
print("product of factorial num is",s)
#i+=1