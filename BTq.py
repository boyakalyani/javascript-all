a=int(input("enter"))
i=1
s=0
while i<a:
    s=s+i
    print(s)
    i+=1



#sum of sqear natural numkbers
# a=int(input("enter"))
# i=1
# s=0
# while i<a:
#     s=s+(i*i)
#     print(s)
#     i+=1


# sum of cube of natural num
# a=int(input("enter"))
# i=1
# s=0
# while i<a:
#     s=s+(i**3)
#     print(s)
#     i+=1



#palindram number
# a=int(input("enter any palindram number"))
# b=a
# s=0
# while a>0:
#     k=a%10
#     a=a//10
#     s=s*10+k
# if b==s:
#     print("its a polindram number")
# else:
#      print("isn't polindram")



a=input("enter")
while a:
    if (a==a[::-1]):
        print("its aplindra")
    else:
        print("not")
    break



# fibonancci series0 to 50
# a=int(input("enter"))
# i=1
# c=0
# a=0
# b=1
# while i<50:
#     c=a+b
#     a=b
#     b=c
#     print(c,",",end="")
#     i+=1




# intered number is perfect or not 
# a=int(input("enter"))
# i=1
# while i<a:
#     if a%i==0:
#         i+=1
# if i==a:
#     print("its aperfect number")
# else:
#     print("its not ")




# factoreal num bers :-
# a=int(input("enter"))
# b=1
# if a>0:
#     for i in range(1,a+1):
#         b=b*i
#         print(b)
# else:
#     print("please enter apositive number")




#rice power
# a=int(input("enr"))
# b=int(input("enter"))
# s=1
# for i in range(1,b+1):
#     s=s*a
#     print(s)


#sum of even odd
# a=int(input("enter"))
# s=0
# s1=0
# for i in range(1,a+1):
#     if i%2==0:
#         s=s+i
#     elif i%2!=0:
#         s1=s1+i
# print("even",s)
# print("odd",s1)        




