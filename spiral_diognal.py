n=int(input())
odd_list=[]
for i in range(1,n+1,2):
    odd_list.append(i)
sum=1
current=1
for i in range(1,len(odd_list)):
    add=odd_list[i]//2+odd_list[i-1]//2+1
    while current<odd_list[i]**2:
        current+=add
        sum+=current
print(sum)