import sqlite3
from . import models

DBNAME = r"e:\classroom\python\demo.db"


# Return DbBook on success or None on failure
def get_book(id):
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select * from books where bookid = ?", id)
        row = cur.fetchone()
        book = models.DbBook(row[0], row[1], row[2], row[3])
        return book
    except Exception as ex:
        print(ex)
        return None
    finally:
        con.close()


def get_all_books():
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select * from books where bookid")
        return cur.fetchall()
    except Exception as ex:
        print(ex)
        return None
    finally:
        con.close()


def get_next_bookid(con):
    cur = con.cursor()
    cur.execute("select max(bookid) + 1 from books")
    row = cur.fetchone()
    cur.close()
    return row[0]


def add_book(title, author, price):
    try:
        con = sqlite3.connect(DBNAME)
        bookid = get_next_bookid(con)
        cur = con.cursor()
        cur.execute("insert into books values(?,?,?,?)", (bookid, title, author, price))
        con.commit()
        if cur.rowcount == 1:
            return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        con.close()
