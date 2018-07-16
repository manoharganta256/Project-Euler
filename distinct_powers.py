a=100
b=100
powers=set()
for i in range(2,a+1):
    for j in range(2,b+1):
        powers.add(i**j)
print(len(powers))