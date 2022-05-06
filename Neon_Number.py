n=int(input())
sum=0
i=n*n
while i>0:
    r=i%10
    sum+=r
    i=i//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")