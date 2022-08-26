unit=int(input("enter the units"))
if unit<=50:
    print(unit*0.50+20/100)
elif unit<=100:
    print(unit*0.75+20/100)
elif unit<=200:
    print(unit*1.20+20/100)
elif unit>=250:
    print(unit*1.50+20/100)
else:
    print("no units")
    


     