signals = 'blue', 'red', 'yellow'

for signal in signals:
    print(signal,len(signal))


for x in range(5):
    print(x, end=' ')

print('\n')
print(list(range(5)))

print(type(range(5)))

print(list(range(0,10,2)))

for x in range(len(signals)):
    print(x, signals[x], len(signals[x]))

nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nest)

for x in range(len(nest)):
    for y in range(len(nest[x])):
        print('nest[', x, '][', y ,']:', nest[x][y])

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

new_squares = [y**2 for y in range(10) ]
print(new_squares)

pairs = []
A = ['blue', 'yellow', 'red']
B = ['red', 'green', 'blue']

for a in A:
    for b in B:
        if a != b:
            pairs.append((a, b))

print(pairs)

new_pairs = [(a, b) for a in A for b in B if a!= b]
print(new_pairs)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print({x: x**2 for x in (2, 4, 6)})