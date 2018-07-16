import numpy as np
n=int(input())
arr=[0]*(n+1)
arr[1]=1
for i in range(2,n+1):
    num=int(i)
    count=0
    while True:
        if (num<=n and arr[num]!=0):
            count+=arr[num]
            break
        elif num%2==0:
            num//=2
        else:
            num=(num*3)+1
        count+=1
    arr[i]=count
m=max(arr)
print(m,arr.index(m))