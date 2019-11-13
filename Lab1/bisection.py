from random import randint

# arr=[-3,1]
# arr=[9,28,23,8,1]
# arr=[8,12,6,1]
arr=[7,-6,-15,-2]
# arr=[-2,-1,-1,-1,-1,5]
# arr=[-2,-1,-1,3,2,1]
# arr=[-6,11,-6,1]
r1=0
r2=0

f1=0
f2=0

e=0.1
while(True):
    
    r1=randint(-100,100)
    r2=randint(-100,100)
    if(r1>r2):
        r1,r2=r2,r1
    print("Guesses are ",r1," and ",r2)
    f1=0
    for i in range(len(arr)):
        f1+=arr[i]*pow(r1,i)

    f2=0
    for i in range(len(arr)):
        f2+=arr[i]*pow(r2,i)
    if(f1*f2<0):
        break
    else:
        print("Wrong Guess")

if(f1==0):
    print(r1)
if(f2==0):
    print(r2)

mid=(r1+r2)/2
midf=0
for i in range(len(arr)):
    midf+=arr[i]*pow(mid,i)
while((midf-int(midf))>e or (r2-r1)>e):
    if(midf*f1>0):
        f1=midf
        r1=mid
    elif(midf*f2>0):
        f2=midf
        r2=mid
    mid=(r1+r2)/2
    midf=0
    for i in range(len(arr)):
        midf+=arr[i]*pow(mid,i)
print("Solution is ",round(mid))