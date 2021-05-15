from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return "<%s(user_name='%s', email='%s')>" \
               % (self.__class__.__qualname__, self.user_name, self.email)
