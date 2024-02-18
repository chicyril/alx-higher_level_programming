#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

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
        dburl = f'mysql+mysqldb://{uname}:{passwd}@localhost/{dbname}'

        engine = create_engine(dburl, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        with Session() as session:
            for state in session.query(State).order_by(State.id):
                print(f'{state.id}: {state.name}')

    except Exception as e:
        print('An error occured: {e}')
