#!/usr/bin/python3
''' Module 1-filter_states that list
    all states beginnig with N '''
import MySQLdb
import sys


if __name__ == "__main__":

    ''' Create the conexion to the database '''
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        database=sys.argv[3]
    )

    ''' Create cursor to execute SQL queries '''
    cursor = db.cursor()

    condition = "SELECT id, name FROM states"
    + "WHERE name LIKE BINARY 'N%' ORDER BY id"

    cursor.execute(condition)

    data = cursor.fetchall()

    ''' Use a for to show all states '''
    for x in data:
        print(x)

    ''' We close the database '''
    db.close()
