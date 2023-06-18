#!/usr/bin/python3
''' This script lists the State object
whose name matches the user's input
from the database, hbtn_0e_6_usa '''


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

    name = sys.argv[4]
    state = session.query(State).\
             filter(State.name == name).order_by(State.id).one_or_none()
    if not state:
        print('Not found')
    else:
        print(f'{state.id}')


if __name__ == '__main__':
    main()
