pockets = [4, 6, 1, 9]
print(pockets)

print(type(pockets))

print(len(pockets))

print(pockets[-3])

pockets[0] = 5
print(pockets)

pockets.append(7)
print(pockets)

pockets.remove(1)
print(pockets)

pockets.insert(1, 3)
print(pockets)

pockets.pop(3)
print(pockets)

pockets.pop()
print(pockets)

pockets.append(1)
pockets.append(2)
pockets.append(4)
print(pockets)

print(pockets[1:3])
print(pockets[:3])
print(pockets[-2:])
print(pockets[:-1])

# value copy: call by value/ call by reference
pockets_copy = pockets
pockets_copy.append(10)
print(pockets_copy)
print(pockets)

print(id(pockets) == id(pockets_copy))
print(pockets is pockets_copy)

pockets_real_copy = pockets[:]
pockets_real_copy.append(11)
print(pockets_real_copy)

print(id(pockets) == id(pockets_real_copy))
print(pockets is pockets_real_copy)
temp_list = [100, 200]
pockets_real_copy.extend(temp_list)
print(pockets_real_copy)

del temp_list[-1]
print(temp_list)
del pockets_real_copy[1:3]
print(pockets_real_copy)

del pockets_copy[:]
print(pockets_copy)

pockets.clear()
print(pockets)

del temp_list
#print(temp_list)

word = '파이썬 문자열 색인'
print(id(word))

word = word[:-2] + '추출'
print(word)

print(id(word))
