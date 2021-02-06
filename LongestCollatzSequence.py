sequences = {}

def nextN(n1):
    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (3 * n1) + 1
    return n2

for x in range(1, 1000001):
    #print(x)
    current = x
    length = 1
    while current != 1:
        if str(current) in sequences:
            length += sequences[str(current)] - 1
            current = 1
        else:
            current = nextN(current)
            length += 1
    sequences[str(x)] = length

values = list(sequences.values())
keys = list(sequences.keys())
print(keys[values.index(max(values))])
print(max(values))