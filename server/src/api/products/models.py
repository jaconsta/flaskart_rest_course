from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from connections.db.base_model import DbBase
from connections.db import db  # session
session = db.session


class Products(DbBase):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    price = Column(Integer)
    sku = Column(String(10))
    picture = Column(Integer, ForeignKey('product_pictures.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return f'Product <{self.id}>: {self.name} - ${self.price}'

    @classmethod
    def create_new(cls, **kwargs):
        product = cls(**kwargs)
        session.add(product)
        session.commit()

    @classmethod
    def save_new(cls, product):
        product = product
        session.add(product)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, product_id):
        return session.query(cls).get(product_id)

    @classmethod
    def update_one(cls, product):
        session.add(product)
        session.commit()

    @classmethod
    def delete_one(cls, product_id):
        product = cls.get_by_id(product_id)
        session.delete(product)
        session.commit()


class ProductPictures(DbBase):
    __tablename__ = "product_pictures"

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    path = Column(String(300))

    def __repr__(self):
        return f'Product picture: <{self.id}>: {self.path}'

    @classmethod
    def create_new(cls, **kwargs):
        picture = cls(**kwargs)
        session.add(picture)
        session.commit()
        return picture

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, file_id):
        return session.query(cls).get(file_id)
