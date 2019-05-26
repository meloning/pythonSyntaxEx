balls = {'red': 4, 'blue': 3, 'green': 5}
print(balls)

print(type(balls))

print(len(balls))

balls['black'] = 1
print(balls)

del balls['green']
print(balls)

print(id(balls))

balls['black'] = 3
print(balls)

print(id(balls))

print(list(balls.keys()))
print(sorted(balls.keys()))
print(list(balls.values()))

print('blue' in balls)
print('white' not in balls)

print(dict([('brown', 3), ('gray', 7)]))
print(dict(brown=3, gray=7))

