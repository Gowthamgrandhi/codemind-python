n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
for i in range(n):
    c=a[i]+b[i]
    d.append(c)
        
print(*d)