n=int(input("enter"))
i=0
reverse=0
while i<n:
    k=n%10
    reverse=reverse*10+k
    n//=10
print(str(reverse)+"reversed numver user is")


# num = 1234
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: " + str(reversed_num))
