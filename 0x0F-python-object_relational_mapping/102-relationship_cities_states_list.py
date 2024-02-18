#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa
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
            for city in session.query(City).order_by(City.id).all():
                print(f'{city.id}: {city.name} -> {city.state.name}')
    except Exception as e:
        print(f'An error occured: {e}')
