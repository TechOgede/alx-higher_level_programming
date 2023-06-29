#!/usr/bin/python3
''' This script lists all State objects and
corresponding City objects contained in the
database, hbtn_0e_6_usa
'''


def main():
    ''' Driver function '''
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import or_
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City)
    states = states.order_by(State.id, City.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')


if __name__ == '__main__':
    main()