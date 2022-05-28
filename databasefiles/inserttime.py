import sqlite3

db_path = "restraunt.db"


def insertime(resid,time):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    try:
        cur.execute("insert into love (resid,time) VALUES('%s','%s')" %(resid,time))
    except:
        return "1"
    
    return "0"