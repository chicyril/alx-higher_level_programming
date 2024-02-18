#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State
from urllib.parse import quote_plus
from sys import argv

if __name__ == '__main__':
    try:
        uname = quote_plus(argv[1])
        passwd = quote_plus(argv[2])
        dbname = quote_plus(argv[3])
        dburl = f'mysql+mysqldb://{uname}:{passwd}@localhost/{dbname}'

        engine = create_engine(dburl, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        with Session() as session:
            new_state = State(name='California')
            session.add(new_state)
            session.flush()
            new_city = City(name='San Francisco', state_id=new_state.id)
            session.add(new_city)
            session.commit()
            print(new_state.cities)

    except Exception as e:
        print(f'An error occured: {e}')
