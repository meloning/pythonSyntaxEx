import sqlite3
from chapter17.select_my_books import select_one_books


def update_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    sql = 'UPDATE my_books SET recommendation=? WHERE title=?'

    cur.execute(sql, (1, '개발자의 코드'))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    select_one_books()
    update_books()
    print('[데이터 수정 완료] ====================')
    select_one_books()