kala=input("enter the action ")
lucky=input("enter the action ")
if kala==lucky:
    print("both are tie ")
elif kala=="rock":
    if lucky=="secssior":
        print("rock is kill to secssiior so kala wil be win")
    else:
        print("paper are coverd the rock so lucky win kala lose")
elif kala=="secssior":
    if lucky=="paper":
        print("secssior cut the paper so kala win")
    else:
        print("rock kill secsssior u lose lucky win")
elif kala=="paper":
    if lucky=="rock":
        print("paper cover rock so kala win")
    else:
        print("secssior cut paper so luvcky lose and secssior not cut rock so kala will be lose")