#!/usr/bin/python3
''' This script lists all State objects from the database, hbtn_0e_6_usa '''


def main():
    ''' Driver function '''
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).all()

    for state in all_states:
        print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    main()
