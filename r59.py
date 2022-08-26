# print(10*2//3**2)


#60
# print(12+34-320+23**2)


#61
# a = 7
# for i in "7":

#      print(a)



#62
# a = "AMIT"
# for i in range(len(a)):

#       print(a)




# 63
# x= "Welcome to my blog"

# j = "i"

# while j in x:

#      print(j)




#64
#print( range (5, 0, -2))




#65
# for i in range(0,2,-1):

#      print("Hello")



#66
# s1="csworld.com"
# s2=""
# s3=""
# for x in s1:
#      if(x=="s" or x=="n" or x=="p"):
#            s2+=x
# print(s2,end=" ")
# print(s3)





#67
# s1="csworld.com"
# c=0
# for x in s1:
#      if(x!="l"):
#          c=c+1
# print(c)




#68
# j=12
# c=9
# while( j):
#      if( j>5):
#            c=c+j-2
#            j=j-1
#      else:
#           break
# print(j, c)
# print(c)




#69
L = [13 , 12 , 21 , 16 , 35 , 7, 4]
s = 5
s1 = 3
for i in L:
     if (i % 4 == 0):
          s = s + i
          continue
     if (i % 7 == 0):
          s1 = s1 + i
print(s , end=" ")
print(s1