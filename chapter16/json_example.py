import json


my_json = {'name': 'junsu', 'job': 'Backend Developer', 'language': ['Korea', 'English']}

print(json.dumps(my_json))

# write
with open('./my_json.json', 'w') as f:
    json.dump(my_json, f)

# read
with open('./my_json.json', 'r') as f:
    new_json = json.load(f)

print(new_json)

# 책 목록 만들기
books = list()

books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'A', '쪽수': 248, '추천유무': True})

for book in books:
    print(book)


with open('./my_books.json', 'w') as f:
    json.dump(books, f, ensure_ascii=False)


with open('./my_books.json', 'r') as f:
    new_books = json.load(f)


for book in new_books:
    print(book)

