from sqlalchemy import String, Integer, Column, ForeignKey, Boolean
from src.settings.settings import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(50))
    password = Column(String(30))

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    private = Column(Boolean)
    owner = Column(ForeignKey(Integer, "user.id"))

    def __str__(self):
        return '{}'.format(self.name)


class UserGroup(Base):
    __tablename__ = 'user_group'
    user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    group = Column(Integer, ForeignKey('group.id'), primary_key=True)

