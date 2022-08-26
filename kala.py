# a=int(input("d"))
# i=0
# while a>i:
#     #i+=1
#     print(i*i)
#     i+=1



# a=int(input("h"))
# i=0
# while a>=i:
#     if a%4==0:
#         if a%100==0:
#             if a%400==0:
#                 print("true")
#             else:
#                 print("false")
#         else:
#             print("false")
    
#     else:
#         print("false")
    # i+=1
    # break
    



a,b=map(str,input().split())
a=int(a)
b=float(b)
if a%5==0 and a+0.5<=b:
    print(b-a-0.5)
else:
    print(b)





