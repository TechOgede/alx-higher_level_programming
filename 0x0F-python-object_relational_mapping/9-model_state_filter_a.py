#!/usr/bin/python3
''' This script lists all State objects from the database, hbtn_0e_6_usa
that contain the letter 'a' '''


def main():
    ''' Driver function '''
    import sys
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

    tab = session.query(State)
    states = tab.filter(or_(State.name.like('a%'),
                            State.name.like('%a'),
                            State.name.like('%a%'))).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    main()
