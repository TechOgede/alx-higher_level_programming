#!/usr/bin/python3
''' This script uses parameterised queries to list vlaues of a state
    in the states table of hbtn_0c_0_usa.
    The state name is passed as command line arg'''


def main():
    ''' lists all states from a database using MySQLdb ORM '''
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    data_base = sys.argv[3]
    state = sys.argv[4]
    query = "SELECT * FROM states WHERE name=%s ORDER BY id"

    db = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                         passwd=pass_word, db=data_base, charset='utf8')
    cur = db.cursor()
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
