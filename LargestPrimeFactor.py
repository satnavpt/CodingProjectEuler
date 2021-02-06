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

print(max(findPrimeFactors(600851475143)))
