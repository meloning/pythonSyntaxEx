import sqlite3
from chapter17.select_my_books import select_all_books


def delete_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    sql = 'DELETE FROM my_books WHERE publisher=?'

    cur.execute(sql, 'A')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    select_all_books()
    delete_books()
    print('[데이터 삭제 완료] ===================')
    select_all_books()