# i=0
# s=0
# g=0
# while i<10:
#     a=int(input("enter"))
#     s=s+a
#     largst=s+10
#     smallst=s/10
#     i+=1
# print("larg number is",largst)
# print("small numbwrs is",smallst)

 


num = float(input("Enter the number: ")) 
maximum = num
minimum = num
count=0
total=0.0

while num == 0:
    count = count + 1
    total = total + num
    num = float(input("Enter the number: "))

if num < minimum:
    minimum = num
else:
    num > maximum
    maximum = num

if count == 0:
    print("max.",max)
else:
    print("Average Number:", round(total/count, 1))
    print("Minimum Number:", minimum)
    print("Maximum Number:", maximum)
# i=0
# s=0
# a=0
# while i<10:
#     b=int(input("enter the bnumbgr"))
#     s=s+b
#     max=s+10
#     i+=1
#     print("maximum number is ",max)