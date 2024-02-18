#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa
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
        Session = sessionmaker(bind=engine)
        with Session() as session:
            state_cities = (session.query(State)
                            .outerjoin(City)
                            .order_by(State.id, City.id)
                            .all())
            for state in state_cities:
                print(f'{state.id}: {state.name}')
                for city in state.cities:
                    if city:
                        print(f'    {city.id}: {city.name}')
    except Exception as e:
        print(f'An error occured: {e}')
