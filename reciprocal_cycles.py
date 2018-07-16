start = 999
found = False
for num in range(start,0,-1):
    numerator = 1
    cycle = set()
    while True:
        r = numerator%num
        if r in cycle:
            break
        cycle.add(r)
        if len(cycle) == num-1:
            found = True
            result = num
            break
        numerator *= 10
    if found:
        break
print(result,len(cycle))