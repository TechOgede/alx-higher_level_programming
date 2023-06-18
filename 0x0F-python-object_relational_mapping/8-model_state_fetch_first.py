#!/usr/bin/python3
''' This script lists the first State
object from the database, hbtn_0e_6_usa '''


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

    state = session.query(State).order_by(State.id).first()

    if not state:
        print('Nothing')
        return

    print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    main()
