import sqlite3


class Setts():


    def __init__(self):
        pass

    def create_general_table(self, folder):
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()

        sql = """CREATE TABLE general (parent_folder text)"""
        sql1 = f'''INSERT INTO general VALUES ("{folder}")'''

        # if database does not exist
        try:
            cursor.execute(sql)
            cursor.execute(sql1)
            conn.commit()
        # if database already exist
        except:
            sql = f'''UPDATE general SET parent_folder="{folder}"'''
            cursor.execute(sql)
            conn.commit()

        conn.close()
        # Still check for errors before returning true
        return True

    def create_server_table(self, id, uip, uname, upath, default_port, port, status):
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()

        try:
            sql = """CREATE TABLE Servers (id real, uip text, \
                uname text,  upath text,  default_port real, \
                port real, status text)"""
            cursor.execute(sql)

        except:
            pass

        sql1 = f'''INSERT INTO Servers VALUES ({id}, "{uip}", \
            "{uname}",  "{upath}",  {default_port}, \
            {port}, "{status}")'''
        cursor.execute(sql1)

        conn.commit()
        conn.close()

    def create_database_table(self, passcode, upath, port):
        username = 'root'
        uip = "127.0.0.1"
        uname = "MySQL"
        default_port = 3306
        status = 'Stopped'

        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()

        try:
            sql = """CREATE TABLE Databases (id real, \
                username text, passcode text, uip text, \
                uname text,  upath text,  default_port real, \
                port real, status text)"""
            cursor.execute(sql)

        except:
            pass

        sql1 = f'''INSERT INTO Databases VALUES ({id}, "{username}", "{passcode}", "{uip}", \
            "{uname}",  "{upath}",  {default_port}, \
            {port}, "{status}")'''
        cursor.execute(sql1)

        conn.commit()
        conn.close()

    def select_general_table(self):
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        sql = """SELECT * FROM general"""
        cursor.execute(sql)
        parent_folder = cursor.fetchone()[0]
        print(parent_folder)
        conn.close()

    def select_server_table(self):
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        sql = """SELECT * FROM Servers"""
        cursor.execute(sql)
        AL = cursor.fetchall()
        conn.close()

    def drop_table(self, table_name):
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        sql = f"""DROP TABLE {table_name}"""
        cursor.execute(sql)
        conn.commit()
        conn.close()
