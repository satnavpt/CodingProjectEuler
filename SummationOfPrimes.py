import time

primeSum = 0

start = time.time()
for num in range(2, 2000000):
    prime = True
    for divisor in range(2, int((num**0.5)+1)):
        if num % divisor == 0:
            prime = False
            break
    if prime == True:
        primeSum += num

print(primeSum)
end = time.time()
print(end - start)