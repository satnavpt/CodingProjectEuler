def findFirstFactor(target):
    factorFound = False
    factors = []

    for divisor in range(2, target):
        if factorFound == False:
            if target % divisor == 0:
                factors.append(divisor)
                factors.append(target//divisor)
                factorFound = True
        else:
            break
    return factors

def findPrimeFactors(target):
    primeFactors = []
    for factor in findFirstFactor(target):
        if findFirstFactor(factor) == []:
            primeFactors.append(factor)
        else:
            for item in findPrimeFactors(factor):
                primeFactors.append(item)
    if primeFactors == []:
        return [target]
    else:
        return primeFactors

target = int(input("Enter the number: "))
nums = list(range(1, target))
occurrences = {}
for num in nums:
    for primeFactor in findPrimeFactors(num):
        count = findPrimeFactors(num).count(primeFactor)
        if str(primeFactor) in occurrences:
            if count >= occurrences[str(primeFactor)]:
                occurrences[str(primeFactor)] = count
        else:
            occurrences[str(primeFactor)] = count

answer = 1
for key, value in occurrences.items():
    print(str(key), str(value))
    answer *= (int(key)**value)

print(answer)
