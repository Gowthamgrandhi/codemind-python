t=int(input())
import math
for i in range (0,t):
    n=int(input())
    root=math.sqrt(n)
    if int(root+0.5)**2==n:
        print("True")
    else:
        print("False");