#!/usr/bin/python3
''' This script creates the State "CAlifornia" with the
City "San Francisco" from the database hbtn_0e_100_usa '''


def main():
    ''' Driver funcion '''
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_fran = City(name='San Francisco')

    california.cities.append(san_fran)

    session.add_all([california, san_fran])

    session.commit()


if __name__ == '__main__':
    main()
