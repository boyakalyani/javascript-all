unit=int(input("enter"))
if unit<=100:
    print("no charge")
elif unit>=100 and unit<=200:
    print((unit-100)*5)
elif unit>=200:
    print((unit-150)*10)
else:
    print("no bil")