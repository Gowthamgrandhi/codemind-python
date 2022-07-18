n,m=map(int,input().split())
if n<m:
    t=m
    m=n
    n=t
for i in range (m,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break