import math

found = False
count = 1
number = []

while found == False and len(number) < 200:
    
    triangular = 0
    for x in range(0, count+1):
        triangular += x

    factors = []

    if triangular % 2 == 0 and triangular % 3 == 0 and triangular % 5 == 0 and triangular % 7 == 0 and triangular % 11 == 0:
        for divisor in range(1, math.floor(triangular**0.5)):
            if triangular % divisor == 0:
                factors.append(divisor)
                factors.append(triangular // divisor)
        print(str(count), str(triangular), str(len(factors)))

        if len(factors) > 500:
            found = True
        
        number.append(len(factors))

    count += 1

print(sum(number) / len(number))
print(max(number))

