# 1단 출력
for x in range(1, 10):
    print('1 *', x, '=', x*1)

# 원하는 구구단 출력
input_val = int(input('구구단 몇단을 출력 할까요? 숫자를 입력하세요: '))

while input_val < 1 or input_val > 9:
    input_val = int(input('구구단은 1단부터 9단까지 출력가능하빈다. 맞는 숫자를 다시 입력하세요: '))

for x in range(1,10):
    print(input_val, '*', x, '=', input_val*x)

# 전체 구구단 출력
for x in range(1,10):
    for y in range(2,10):
        print(y, '*', x, '=', y*x, end="\t")
    print("\n")