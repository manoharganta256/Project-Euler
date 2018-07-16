from math import sqrt,ceil
def div_sum(num):
    result = 0
    for i in range(2,int(sqrt(num))+1):
        if num%i == 0:
            if i == (num//i):
                result += i
            else:
                result += (i + num//i)
    return result+1
abudent = []
for i in range(12,28123+1):
    if div_sum(i) > i:
        abudent.append(i)
chart = [False]*28124
result = 0
for i in range(len(abudent)):
    for j in range(i,len(abudent)):
        if abudent[i] + abudent[j] < 28124:
            chart[abudent[i]+abudent[j]] = True
        else:
            break
for i in range(1,len(chart)):
    if not chart[i]:
        result += i
print(result)