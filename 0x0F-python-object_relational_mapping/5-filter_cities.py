#!/usr/bin/python3
''' This script lists the  cities in a given state
    from the database hbtn_0c_0_usa '''


def main():
    ''' lists the cities in a given state
        from a database using MySQLdb ORM '''
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    data_base = sys.argv[3]
    city = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                         passwd=pass_word, db=data_base, charset='utf8')
    cur = db.cursor()
    query = "SELECT cities.name\
             FROM cities JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s\
             ORDER BY cities.id"
    cur.execute(query, (city,))
    row = cur.fetchall()

    cities = []
    for col in row:
        cities.append("".join(col))
    row = ", ".join(cities)
    print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
