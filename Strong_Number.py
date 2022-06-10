n=int(input())
m=n
sum=0
import math
while n!=0:
    r=n%10
    sum+=math.factorial(r)
    n=n//10
if(sum==m):
    print("The number", m, "is a strong number")
else:
    print("The number",m,  "is not a strong number")