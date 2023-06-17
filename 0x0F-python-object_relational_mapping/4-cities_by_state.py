#!/usr/bin/python3
''' This script lists all cities by states from the database hbtn_0c_0_usa '''


def main():
    ''' lists all cities by states from a database using MySQLdb ORM '''
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    data_base = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                         passwd=pass_word, db=data_base, charset='utf8')
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states ON cities.state_id = states.id\
             ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
