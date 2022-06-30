n=int(input())
arr=list(map(int,input().split()))
os=0
es=0
for i in range(n):
    if i%2==0:
        os+=arr[i]
    else:
        es+=arr[i]
print(os-es)