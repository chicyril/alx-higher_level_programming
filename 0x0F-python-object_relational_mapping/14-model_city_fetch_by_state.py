#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from urllib.parse import quote_plus
import sys

if __name__ == '__main__':
    try:
        uname = quote_plus(sys.argv[1])
        passwd = quote_plus(sys.argv[2])
        dbname = quote_plus(sys.argv[3])
        dburl = f'mysql+mysqldb://{uname}:{passwd}@localhost/{dbname}'
        engine = create_engine(dburl, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        State.cities = relationship("City",
                                    order_by=City.id,
                                    back_populates='state')

        Base.metadata.create_all(engine)

        with Session() as session:
            for city in session.query(City).order_by(City.id):
                print(f'{city.state.name}: ({city.id}) {city.name}')

    except Exception as e:
        print(f'An error occured: {e}')
