#!/usr/bin/python3
''' Module 4-cities_by_state  '''
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

    ''' Use mark % to avoid sql injections '''
    sql = "SELECT a.id, a.name, b.name FROM cities a \
            LEFT JOIN states b ON a.state_id = b.id ORDER BY a.id"

    cursor.execute(sql)

    row = cursor.fetchall()

    ''' Use a for to show all states '''
    for x in row:
        print(x)

    ''' We close the database '''
    db.close()
