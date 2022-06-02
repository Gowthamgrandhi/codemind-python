n=int(input())
a=list(map(int,input().split()))
s=int(input())
f=0
for i in a:
    if i==s:
        f=1
        break
    else:
        f=0
if f==1:
    print(True)
else:
    print(False)