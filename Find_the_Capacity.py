s,t,b=map(int,input().split())
res=2*s*t*b*512
res1=res//1024
print(res1,end='KB')