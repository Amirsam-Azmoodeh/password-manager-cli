import sqlite3


def add(service , username , password) :
        with sqlite3.connect('DataBase.db') as con :
                cursor = con.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS passwords (ID INTEGER PRIMARY KEY , Service TEXT, Username TEXT, Password TEXT)')
                cursor.execute('INSERT INTO passwords (Service , Username , Password ) VALUES(? , ? , ? )' , (service , username , password))
                con.commit()

def get(service , username) :
        with sqlite3.connect('DataBase.db') as con :
                cursor = con.cursor()
                cursor.execute('SELECT * FROM passwords WHERE Service = ? AND Username = ?' , (service , username , ))
                return cursor.fetchall()
        
def delete(username) :
        with sqlite3.connect('DataBase.db') as con :
                cursor = con.cursor()
                cursor.execute('DELETE FROM passwords WHERE  Username = ?' , (username ,))
                con.commit()

def list() :
        with sqlite3.connect('DataBase.db') as con :
                cursor = con.cursor()
                cursor.execute('SELECT * FROM passwords')
                return cursor.fetchall()



    
        