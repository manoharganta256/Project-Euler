import math
n=int(input())
res=0
while n%2==0:
    res=2
    n//=2
for i in range(3,math.floor(math.sqrt(n))+1,2):
    while n%i==0:
        res=i
        n//=i
if n>2:
    res=n
print(res)