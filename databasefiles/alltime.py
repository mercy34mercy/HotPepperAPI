import sqlite3

db_path = "restraunt.db"


def alltime():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    try:
        cur.execute("select * from love")
        res = cur.fetchall()
    except:
        return 1
    
    return res