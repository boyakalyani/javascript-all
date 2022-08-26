p=10
q=20
p=p*q//4
q=p+q**3
print(p,q)

X,Y,Z=map(int,input().split())
print(X-Y,(X-Y)-Z)


a=int(input("en"))
b=int(input("en"))
c=int(input("en"))
print(a-b,(a-b)-c)

N, A, B = map(int, input().split())
T = N-A
P = A+B
print(T, P)


w,x,y,z=map(int,input().split())
t=int(input(""))
while t>0:
    b=w+y*z
    if b>x:
        print("over flow")
    elif b==x:
        print("filled")
    else:
        print("unfilled")
    
        
        
        
        
        
