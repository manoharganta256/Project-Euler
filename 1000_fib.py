n=int(input())
fib=[0,1]
while len(str(fib[-1]))!=n:
    fib.append(fib[-1]+fib[-2])
print(len(fib)-1)