import sqlite3

def create_table():
    conn = sqlite3.connect('settings.db')
    cursor = conn.cursor()

    sql = """CREATE TABLE general (parent_folder text)"""
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        pass

    conn.close()

