from sqlalchemy import String, Integer, Column, ForeignKey, Text
from src.settings.settings import Base


class Poll(Base):
    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(Text(300))
    author = Column(Integer, ForeignKey("user.id"))
    group = Column(Integer, ForeignKey('group.id'))


class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    content = Column(Text(200))


class Vote(Base):
    __tablename__ = 'votes'
    user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    option = Column(Integer, ForeignKey('option.id'), primary_key=True)
