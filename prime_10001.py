from math import sqrt
from timeit import default_timer
primes=[2]
n=int(input())
start=default_timer()
number=3
while len(primes)<n:
    prime=True
    for i in range(len(primes)):
        if primes[i]>int(sqrt(number)):
            break
        elif number%primes[i]==0:
            prime=False
            break
        else:
            continue
    if prime:
        primes.append(number)
    number+=2
print(primes[-1])
elapsed=default_timer()-start
print(elapsed)