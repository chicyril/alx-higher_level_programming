#!/usr/bin/python3
"""Change the name of a State object from the database hbtn_0e_6_usa"""
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
            mod_state = session.query(State).filter(State.id == 2).first()
            if mod_state:
                mod_state.name = 'New Mexico'
                session.commit()

    except Exception as e:
        print(f'An error occured {e}')
