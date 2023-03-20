import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_last_input(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM soccer_app_player ORDER BY id DESC LIMIT 1;")

    rows = cur.fetchall()

    for row in rows:
        #print(row)
        return row





def main():
    database = "db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:

        print("Quering last user player input...")
        return select_last_input(conn)


if __name__ == '__main__':
    main()


