from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model import User, Music


engine = create_engine("postgresql+psycopg2://dashalin:GP08139035@localhost/test2DB")
# engine = create_engine("postgresql+psycopg2://postgres:GP08139035@db/test2DB")

session = Session(bind=engine)


def create_user(name, token):
    q = User(name=name, uuid=token)
    session.add(q)
    session.commit()
    user_id = session.query(User).order_by(User.id.desc()).first()
    return user_id.id


def create_song(user_id, name, uuid):
    q = Music(name=name, user_id=user_id, uuid=uuid)
    session.add(q)
    session.commit()
    song_id = session.query(User).order_by(User.id.desc()).first()
    return song_id.id


def get_user(user_id):
    uuid = session.query(User).get(user_id)
    return uuid.uuid


# def get_last_answer():
#     try:
#         obj = session.query(Question).order_by(Question.id.desc()).first()
#         obj = obj.answer
#     except Exception:
#         obj = ''
#     return obj