n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in a:
    c=a.count(b)
print(c)