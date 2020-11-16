import sqlite3


def create_general_table(folder):
    conn = sqlite3.connect('settings.db')
    cursor = conn.cursor()

    sql = """CREATE TABLE general (parent_folder text)"""
    sql1 = f'''INSERT INTO general VALUES ("{folder}")'''

    # if database does not exist
    try:
        cursor.execute(sql)
        cursor.execute(sql1)
        conn.commit()
        print('not exist')
    # if database already exist
    except:
        sql2 = f'''UPDATE general SET parent_folder="{folder}"'''
        cursor.execute(sql2)
        conn.commit()
        print('exist')

    conn.close()


def select_general_table():
    conn = sqlite3.connect('settings.db')
    cursor = conn.cursor()
    sql = """SELECT * FROM general"""
    cursor.execute(sql)
    parent_folder = cursor.fetchone()[0]
    print(parent_folder)
    conn.close()


select_general_table()
