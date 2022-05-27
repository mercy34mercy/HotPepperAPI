import sqlite3
import uuid

db_path = "restraunt.db"


def sql(name):
    print(name)
    uid = str(uuid.uuid4()).replace("-", "")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "Create table restraunt(name varchar(300) unique, resid  varchar(100) PRIMARY KEY)")


sql("まもなく釜山駅")
