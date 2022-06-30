n,m=map(int,input().split())
for i in range(2,n*m+1):
    if i%n==0 and i%m==0:
        print(i)
        break