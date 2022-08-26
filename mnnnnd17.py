n=int(input("enter"))
s=0
k=n
l=len(str(n))
while k>0:
    digit=k%10
    k//=10
    s=s+digit**l
if s==n:
    print(n,"this is arm srtron")
else:
    print(n,"tyhis is not arm stron")


n=int(input("enter"))
# s=0
# k=n
# l=len(str(k))
# while k>0:
#     j=k%10
#     k//=10
#     s=s+j**l
# if s==n:
#     print(n,"this is arm strong")
# else:
#     print(n,"this not arm strong")

# i=0
# s=0
# while i<=10:
#     a=int(input("enter the number"))
#     s
#     if ==9:
#         print("maximum number is ",i)
#         break
#     i+=1