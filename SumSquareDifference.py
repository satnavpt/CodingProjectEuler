target = int(input("Enter an upper limit: "))

sumOfSquares = 0
sumOfNums = 0
for num in range(1, target+1):
    sumOfSquares += num**2
    sumOfNums += num

squareOfSums = sumOfNums**2

diff = squareOfSums - sumOfSquares

print(diff)
