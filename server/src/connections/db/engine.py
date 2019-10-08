from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from .base_model import DbBase

engine = create_engine('sqlite:///flaskart.sqlite')

Session = sessionmaker(bind=engine)


def init_db():
    DbBase.metadata.create_all(engine, checkfirst=True)


def drop_db():
    DbBase.metadata.drop_all(engine, checkfirst=True)


class Db:
    engine = None
    Session = None
    session = None

    def __init__(self, db_url=None):
        if db_url:
            self.connect(db_url)

    def connect(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.Session)

    def disconnect(self):
        self.session.remove()

    def init_db(self):
        DbBase.metadata.create_all(self.engine, checkfirst=True)

    def drop_db(self):
        DbBase.metadata.drop_all(self.engine, checkfirst=True)
