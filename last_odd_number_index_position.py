a=int(input())
arr=list(map(int,input().split()))
ind=0
for i in range(a):
    if arr[i]%2!=0:
        ind=i
print(ind)