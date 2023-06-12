import psycopg2
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database


engine = create_engine("postgresql+psycopg2://dashalin:GP08139035@localhost/test2DB")
# engine = create_engine("postgresql+psycopg2://postgres:GP08139035@db/test2DB")

if not database_exists(engine.url):
    create_database(engine.url)

engine.connect()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    uuid = Column(String(150), nullable=False, unique=True)


class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    user_id = Column(
        Integer,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False
    )
    uuid = Column(String(150), nullable=False)


Base.metadata.create_all(engine)
