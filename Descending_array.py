n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=a[::-1]
aa=sorted(a)
if aa==c:
    print("yes")
else:
    print("no")