from math import pow
power = 5
limit = int(sum(pow(i,power) for i in [9]*(power+1)))
result = 0
for i in range(10,limit):
    if i == int(sum(pow(i,power) for i in map(int,list(str(i))))):
        result += i
print(result)