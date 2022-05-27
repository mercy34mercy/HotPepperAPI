import sqlite3
import uuid

db_path = "restraunt.db"

def insertres(name):
    print(name)
    uid = str(uuid.uuid4()).replace("-","")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    print(uid)
    try:
        cur.execute("insert into restraunt(name,resid) VALUES('%s','%s')" %(name,uid))
        conn.commit()
        return uid

    except Exception as e:
        # TODOインサートできなかったときセレクトしてくる
        try:
            cur.execute("SELECT resid from restraunt where name = '%s'" %(name))
            conn.commit()
            data = cur.fetchone()
            print(data[0])
            return data[0]
        except Exception as e:

            print(str(e))
            return "err"
        
    