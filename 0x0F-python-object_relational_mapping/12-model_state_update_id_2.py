#!/usr/bin/python3
''' This script updates  a State object
in the database, hbtn_0e_6_usa '''


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

    state = session.query(State).filter(State.id == 2).one()

    state.name = 'New Mexico'

    session.commit()


if __name__ == '__main__':
    main()
