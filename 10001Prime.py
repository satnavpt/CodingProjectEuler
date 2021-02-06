import time

primes = []
num = 2

start = time.time()

while len(primes) != 10001:
    prime = True
    numsToCheck = range(2, int((num**0.5)+1))
    for divisor in numsToCheck:
        if num % divisor == 0:
            prime = False
            break
    if prime == True:
        primes.append(num)
    num += 1

print(primes[10000])
end = time.time()
print(end - start)