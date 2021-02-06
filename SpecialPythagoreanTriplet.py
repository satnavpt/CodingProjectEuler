triplets = []

for a in range(1, 998):
    for b in range(1, 998):
        cSquared = a**2 + b**2
        c = cSquared**0.5
        if c.is_integer():
            c = int(c)
            triplets.append([a, b, c])
            #print(str(a) + "^2 + " + str(b) + "^2 = " + str(int(c)) + "^2")

for triplet in triplets:
    if triplet[0] + triplet[1] + triplet[2] == 1000:
        answer = triplet[0] * triplet[1] * triplet[2]
        print(answer)

