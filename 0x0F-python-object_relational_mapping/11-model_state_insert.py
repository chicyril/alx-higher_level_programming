#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database `hbtn_0e_6_usa`"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from urllib.parse import quote_plus


if __name__ == '__main__':
    try:
        uname = quote_plus(sys.argv[1])
        passwd = quote_plus(sys.argv[2])
        dbname = quote_plus(sys.argv[3])
        dburl = f'mysql+mysqldb://{uname}:{passwd}@localhost/{dbname}'
        engine = create_engine(dburl, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        with Session() as session:
            new_state = State(name='Louisiana')
            session.add(new_state)
            session.commit()
            print(new_state.id)
    except Exception as e:
        print(f"An error occured: {e}")
