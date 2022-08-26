# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print("The total sum of digits is:",tot)

n=int(input("enter"))
s=0
i=0
while i<n:
    k=n%10
    n=n//10
    s=s+k
print(s,"sum of digits")
    