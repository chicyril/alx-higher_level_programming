#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database
`hbtn_0e_6_usa`."""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import sys

if __name__ == '__main__':
    try:
        uname = quote_plus(sys.argv[1])
        passwd = quote_plus(sys.argv[2])
        dbname = quote_plus(sys.argv[3])
        state_name = sys.argv[4]
        dburl = f'mysql+mysqldb://{uname}:{passwd}@localhost/{dbname}'
        engine = create_engine(dburl, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        with Session() as session:
            state = (session
                     .query(State)
                     .filter(State.name == state_name)
                     .first())
            if state:
                print(f'{state.id}')
            else:
                print('Not found')
    except Exception as e:
        print(f'An error occured: {e}')
