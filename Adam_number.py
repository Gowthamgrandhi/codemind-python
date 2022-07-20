n=input()
m=int(n)*int(n)
m1=str(m)
r2=n[::-1]
m2=int(r2)*int(r2)
m3=str(m2)
r=m3[::-1]
if int(m)==int(r):
    print(True)
else:
    print(False)
