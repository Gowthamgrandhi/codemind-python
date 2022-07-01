n=int(input())
rev=0
t=n
while(n!=0):
    if n<0:
        n=n*-1
        r=n%10
        rev=rev*10+r
        n=n//10
    else:
        r=n%10
        rev=rev*10+r
        n=n//10
if t<0:
    print(-rev)
else:
    print(rev)