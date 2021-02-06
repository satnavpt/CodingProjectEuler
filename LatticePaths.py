import math

dimension = int(input("Enter a number:  "))

paths = (math.factorial(2*dimension)) // (math.factorial(dimension))**2

print(paths)