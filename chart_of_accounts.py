import sqlite3

def connect():
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS chart_of_accounts (id INTEGER PRIMARY KEY, AccNumber integer, Account text)")
    conn.commit()
    conn.close()

def insert(AccNumber, Account):
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM chart_of_accounts")
    list_account=cur.fetchall()
    conn.close
    def check(AccNumber):
        for i in list_account:
            if AccNumber in i:
                return "Account already exists"
            
    checked = check(AccNumber)
    
    if checked == None:
        cur.execute("INSERT INTO chart_of_accounts VALUES (NULL,?,?)",(AccNumber, Account))
        conn.commit()
    else:
        print(checked)
    
   
def view():
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM chart_of_accounts")
    rows=cur.fetchall()
    conn.close()
    for i in rows:
        print(i)

def search(AccNumber="", Account=""):
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM chart_of_accounts WHERE AccNumber=? OR Account=?", (AccNumber, Account))
    rows=cur.fetchall()
    conn.close()
    return rows

def update(id, AccNumber, Account):
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("UPDATE chart_of_accounts SET AccNumber=?, Account=? WHERE id=?",(AccNumber, Account, id))
    conn.commit()
    conn.close
    
def delete(AccNumber="",Account=""):
    conn=sqlite3.connect("chart_of_accounts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM chart_of_accounts WHERE AccNumber=? or Account=?",(AccNumber, Account))
    conn.commit()
    conn.close()
   
connect() 
