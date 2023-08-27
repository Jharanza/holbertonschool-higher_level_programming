#!/usr/bin/python3
''' Module 0-select_states that connect python to a database '''
import MySQLdb


if __name__ == "__main__":

    ''' Create the conexion to the database '''
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="hbtn_0e_0_usa"
    )

    ''' Create cursor to execute SQL queries '''
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id")

    ''' Use a for to show all states '''
    for x in cursor:
        print(x)

    ''' We close the database '''
    db.close()
