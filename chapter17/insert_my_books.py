import sqlite3

# 데이터 입력 함수
def insert_books():
    conn = sqlite3.connect('my_books.db')

    cur = conn.cursor()

    cur.execute("INSERT INTO my_books VALUES ('개발자의 코드', '2013.02.28', 'A', 200, 0)")

    sql = 'INSERT INTO my_books VALUES (?, ?, ?, ?, ?)'

    cur.execute(sql, ('클린 코드', '2010.03.04', 'B', 584, 1))

    books = [
        ('빅데이터 마케팅', '2014.07.02', 'A', 296, 1),
        ('구글드', '2010.02.10', 'B', 526, 0),
        ('강의력', '2013.12.12', 'A', 248, 1)
    ]

    cur.executemany(sql, books)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_books()

