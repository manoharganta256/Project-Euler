l=[i*j for i in range(110,1000,11) for j in range(110,1000,11) if str(i*j)==str(i*j)[::-1]]
print(max(l))