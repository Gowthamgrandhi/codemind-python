n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
j=0
s=0
for i in b:
    s+=i*2**j
    j+=1
print(s)