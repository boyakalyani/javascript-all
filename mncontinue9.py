count=0
str="navgurukul"
while count<len(str):
     count+=1
     if str[count]=="a":
         continue
     if str[count]=="u":
         continue
     print(str[count])
print("the endf ",str[count])




i=0
while i<=9:
    i+=1
    if i==5:
        print("skippede element",i)
        continue
    print(i)
