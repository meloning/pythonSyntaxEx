import sqlite3


def select_all_books():

    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print(' [1] 전체 데이터 출력')

    books = cur.fetchall()

    for book in books:
        print(book)

    conn.close()


def select_some_books(number):

    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print(' [2] 데이터 일부 출력')
    books = cur.fetchmany(number)

    for book in books:
        print(book)

    conn.close()


def select_one_books():

    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print(' [3] One 데이터 출력')
    print(cur.fetchone())

    conn.close()


def find_big_books():

    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT title, pages FROM my_books WHERE pages > 300')

    print(' [4] 페이지 많은 책 출력')
    books = cur.fetchall()

    for book in books:
        print(book)

    conn.close()


if __name__ == '__main__':
    select_all_books()
    print('=====================================')
    select_some_books(3)
    print('=====================================')
    select_one_books()
    print('=====================================')
    find_big_books()