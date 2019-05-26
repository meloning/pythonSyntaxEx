def daily_working_hours(hours=None):
    if hours == None:
        print('인자 값 세팅을 잊으셨군요.')
    return hours

daily_working_hours()

def introduce_my_car(manufacturer, seats=4, type='sedan'):
    print('내 차는', manufacturer, '의', seats, '인승', type, '이다.')

introduce_my_car('AvanThe')

# 가변인자 리스트
def introduce_your_family(name, *family_names, **family_info):
    print('제 이름은', name, '입니다. ')
    print('제 가족들의 이름은 아래와 같아요.')
    for name in family_names:
        print(name)
        print("-" * 40)
    for key in family_info.keys():
        print(key, ":", family_info[key])

introduce_your_family('Chris', 'Jihee', 'Anna', 'Shinhoo', 집='용인', 가훈='행복하게 살자!')

def concat(*args, sep='/'):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# 연패킹 인자 리스트
print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

# Error keywords must be strings
inputs = {'manufacturer': '현대', 'seats': 9, type: '승합차'}
# introduce_my_car(**inputs)

# 변수 범위
# 지역변수 [ _변수명 ]
# 전역변수 [ global 변수명 ]

def my_function():
    """아무고토 하기시루떡"""
    pass

print(my_function.__doc__)