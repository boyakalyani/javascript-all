# counter=0
# str="navgurukul"
# while counter<len(str):
#     counter+=1
#     if str[counter]=="a":
#         continue
#     if str[counter]=="u":
#         continue
#     print(str[counter])
# print("the end ",str[counter])


# i=1
# count=0
# a=int(input("enter"))
# while i<=a:
#     j=1
#     b=0
#     while j<=i:
#         if i%j==0:
#             b+=1
#         j+=1
#     if b==2:i
#         count+=1
#         print("prime",i)
#     i+=1


a=int(input("ente"))
i=1
c=0
while i<=a:
    if a%i==0:
        c+=1
    i+=1
if c==2:
    print("primee")
else:
    print("not pime")