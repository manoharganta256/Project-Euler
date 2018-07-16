from itertools import permutations
n=int(input())
num_list=list(map(str,range(0,n)))
arr=[]
for i in permutations(num_list):
    arr.append(int(''.join(i)))
#arr.sort()
print(arr)