def isautomorphic(n):
    sq=n*n
    while(n>0):
        if(n%10!=sq%10):
            return False
        n=n//10
        sq=sq//10
    return True
        
n=int(input())
if isautomorphic(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")