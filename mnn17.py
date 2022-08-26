i=1
while i<5:
    a=int(input("enter num"))
    i+=1
    if a<5:
        print("num entered by you enteed is small try one more time")
    elif a==5:
        print("wow you guessed the currect num")
        break
    else:
        print("num entered is grester try one more time")
    