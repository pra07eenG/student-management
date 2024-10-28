import sqlite3
def create_db():
    conn=sqlite3.connect(database="srms.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (roll_no INTEGER PRIMARY KEY,name text,course text,department text,year text,semester text,dob text,email text,parents_no text,address text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS courses (cid INTEGER PRIMARY KEY AUTOINCREMENT,course text,year text,semester text,department text,subject text,subject_code text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS attendence (aid INTEGER PRIMARY KEY ,course text,year text,department text,absentees text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS login (lid INTEGER PRIMARY KEY ,username text,password text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS results (rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,subject text,marks_ob text,full_marks text,per text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS signin (lid INTEGER PRIMARY KEY ,username text,password text)")
    conn.commit()

    conn.close()

def show():
    conn=sqlite3.connect(database="srms.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    print("rows of student table :",rows)

    cur.execute("SELECT * FROM courses")
    rows=cur.fetchall()
    print("rows of courses table :",rows)
    conn.commit()

    cur.execute("SELECT * FROM attendence")
    rows=cur.fetchall()
    print("rows of attendence table :",rows)
    conn.commit()

    cur.execute("SELECT * FROM login")
    rows=cur.fetchall()
    print("rows of login :",rows)
    conn.commit()

    cur.execute("SELECT * FROM results")
    rows=cur.fetchall()
    print("rows of results :",rows)
    conn.commit()

    cur.execute("SELECT * FROM signin")
    rows=cur.fetchall()
    print("rows of sign in :",rows)
    conn.commit()

    return rows


def insert():
    conn=sqlite3.connect(database="srms.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO LOGIN (username, password) VALUES ('krishnavi','12345')")
    conn.commit()

    cur.execute("INSERT INTO SIGNIN (username, password) VALUES ('hello','123')")
    conn.commit()

    conn.close()

def delete():
    conn=sqlite3.connect(database="srms.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM login")
    conn.commit()
    conn.close()


create_db()
show()
#insert()
#delete()