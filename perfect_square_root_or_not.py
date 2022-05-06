import math
n=int(input())
a=round(math.sqrt(n),2)
if n==a*a:
    print("True")
else:
    print("False")