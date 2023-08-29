#!/usr/bin/python3
''' Module 5-filter_cities '''
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
    sql = "SELECT a.name FROM cities a LEFT JOIN states b \
            ON a.state_id = b.id WHERE b.name = %s ORDER BY a.id"

    data = (str(sys.argv[4]),)

    cursor.execute(sql, data)

    row = cursor.fetchall()

    ''' Use a for to show all states '''
    for x in row:
        print(x)

    ''' We close the database '''
    db.close()
