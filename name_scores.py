import re
pattern = re.compile('[A-Z]+')
file = open('names.txt','r')
names = []
for line in file:
    names += pattern.findall(line)
names.sort()
count = 0
for i in range(len(names)):
    temp = 0
    for alpha in list(names[i]):
        temp += ord(alpha) - ord('A') + 1
    count += (i+1)*temp
print(count)