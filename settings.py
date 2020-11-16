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

    def select_general_table():
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        sql = """SELECT * FROM general"""
        cursor.execute(sql)
        parent_folder = cursor.fetchone()[0]
        print(parent_folder)
        conn.close()


select_general_table()
