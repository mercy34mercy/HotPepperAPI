import sqlite3
import uuid

db_path = "restraunt.db"

def insertres(name):
    print(name.replace(" ","").replace("　",""))
    uid = str(uuid.uuid4()).replace("-","")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print(uid)
    try:
        cur.execute("insert into restraunt(name,resid) VALUES('%s','%s')" %(name,uid))
        # cur.execute("drop restraunt)")
        # cur.execute("Create table restraunt(name varchar(300)  PRIMARY KEY, resid  varchar(200))")

    except Exception as e:
        # TODOインサートできなかったときセレクトしてくる
    
        conn.commit()
    return uid