t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    if sorted(a)==a:
        print('0')
    else:
        print(max(a)-min(a))