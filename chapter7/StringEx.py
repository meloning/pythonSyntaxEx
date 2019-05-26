"""
c = input('영어 대소문자로 이루어진 문장을 입력하세요.')

print('모두 대문자로 출력\n', c.upper())
print('모두 소문자로 출력\n', c.lower())

new_s = str()

for s in c:
    if s.lower():
        new_s += s.upper()
    else:
        new_s += s.lower()

print('대소문자 바꿔서 출력\n' + new_s)

print('대소문자 바꿔서 출력\n' + c.swapcase())
"""

"""
# String reverse

i = input('영어 문장을 입력하세요\n')

new_i = str()

for x in range(len(i)-1, -1, -1):
    new_i += i[x]

print(new_i)

print(i[::-1])
"""

# 책 목록 만들기
books = list()

books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'A', '쪽수': 248, '추천유무': True})

for book in books:
    print(book)

many_page = list()
recommends = list()
all_pages = int()
pub_companies = set()

for book in books:

    if book['쪽수'] > 250:
        many_page.append(book['제목'])
    if book['추천유무']:
        recommends.append(book['제목'])
    all_pages = all_pages + book['쪽수']
    pub_companies.add(book['출판사'])

# many_page = [book['제목'] for book in books if book['쪽수'] > 250]
# recommends = [book['추천유무'] for book in books if book['추천유무']]

print('쪽수가 250쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)