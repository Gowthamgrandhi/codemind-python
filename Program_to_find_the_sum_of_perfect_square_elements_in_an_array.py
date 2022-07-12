import math
n=int(input())
a=list(map(int,input().split()))
su=0
for i in a:
    s=int(math.sqrt(i))
    if s*s==i:
        su+=i
print(su)