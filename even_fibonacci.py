n=int(input())
l=[0,1]
sum=0
for i in range(n):
    l.append(l[i]+l[i+1])
    if l[-1]>n:
        break
    if l[-1]%2==0:
        sum+=l[-1]
print(sum)