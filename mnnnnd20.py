# m=""
# a=int(input("enter "))
# t=a
# while a>0:
#     k=a%10
#     a//=10                                                          
#     m=m+str(k)
# if int(m)==t:
#     print("it is a polindram")
# else:
#     print("isnt polindram")




a=input("enter")
if (a==a[::-1]):
    print("this is apolindram")
else:
    print("this is not polindram")

 
a=int(input("entre"))
b=" "
c=a
while a>0:
    k=a%10
    a//=10
    b=b+str(k)
if int(b)==c:
    print("polindram")
else:
    print("isnt polindram")