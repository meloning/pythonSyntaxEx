# Set 순서없이 중복 미허용

lang = {'java', 'java', 'python', 'C++', 'python'}
print(lang)

print('java' in lang)

print('javascript' in lang)

a = set('abracadabra')
b = set('alacazam')
print(a)

print(a-b)

print(a|b)

print(a&b)

print(a^b)
