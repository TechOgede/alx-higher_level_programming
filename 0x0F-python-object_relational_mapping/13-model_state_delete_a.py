#!/usr/bin/python3
''' This script deletes State objects from the database, hbtn_0e_6_usa
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
    tab.filter(or_(State.name.like('a%'),
                   State.name.like('%a'),
                   State.name.like('%a%'))).delete(synchronize_session=False)

    session.commit()


if __name__ == '__main__':
    main()
