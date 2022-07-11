n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if a.count(i)==1:
        d.append(i)
if d==[]:
    print(-1)
else:
    print(*d)