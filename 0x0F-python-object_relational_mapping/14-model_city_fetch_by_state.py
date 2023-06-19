#!/usr/bin/python3
''' This script lists all City objects from the database, hbtn_0e_6_usa
'''


def main():
    ''' Driver function '''
    import sys
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import or_
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in res:
        print(f'{state.name}: ({city.id}) {city.name}')


if __name__ == '__main__':
    main()
