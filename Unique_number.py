n=int(input())
flag=1
I=[]
while n>0:
    r=n%10
    if r not in I:
        I.append(r)
    else:
        flag=0
        break
    n=n//10
if (flag==1):
    print("Unique Number")
else:
    print("Not Unique Number")