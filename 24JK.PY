char=input("enter the character")
if char>="a" and char<="z" or char>="A" and char<="Z":
    print("alfhabet")
elif char>="0" and char<="9":
    print("digit")
else:
    print("special character")